import numpy as np
import json

class MBTILoader:
    @staticmethod
    def load_json_data(filepath):
        with open(filepath, 'r') as file:
            data = json.load(file)
        return data

class MBTITransformer:
    @staticmethod
    def transform_mbti(input_json):
        mbti_vector = [
            1 - input_json.get('I', 0) if 'I' in input_json else input_json.get('E', 0),
            1 - input_json.get('N', 0) if 'N' in input_json else input_json.get('S', 0),
            1 - input_json.get('T', 0) if 'T' in input_json else input_json.get('F', 0),
            1 - input_json.get('J', 0) if 'J' in input_json else input_json.get('P', 0)
        ]
        return {
            "name": input_json["user"],
            "mbti": mbti_vector
        }

class CosineSimilarity:
    @staticmethod
    def calculate_similarity(vec1, vec2):
        dot_product = np.dot(vec1, vec2)
        norm_vec1 = np.linalg.norm(vec1)
        norm_vec2 = np.linalg.norm(vec2)
        cosine_sim = dot_product / (norm_vec1 * norm_vec2)
        return cosine_sim

class ActivityRecommender:
    def __init__(self, user_mbti_file, activities_file):
        self.user_mbti_file = user_mbti_file
        self.activities_file = activities_file

    def recommend_activities(self):
        original_user_mbti_data = MBTILoader.load_json_data(self.user_mbti_file)
        transformed_user_mbti_data = MBTITransformer.transform_mbti(original_user_mbti_data)
        
        activities_data = MBTILoader.load_json_data(self.activities_file)
        
        user_mbti_vector = np.array(transformed_user_mbti_data["mbti"])
        user_name = transformed_user_mbti_data["name"]
        
        recommendations = []
        for activity, vector in activities_data.items():
            similarity = CosineSimilarity.calculate_similarity(user_mbti_vector, np.array(vector))
            if similarity >= 0.9:
                recommendations.append(activity)
        return user_name, recommendations

if __name__ == "__main__":
    # 파일 경로 지정
    user_mbti_file = './user_mbti.json'
    activities_file = './activities.json'

    # 추천 운동 리스트
    recommender = ActivityRecommender(user_mbti_file, activities_file)
    user_name, recommendations = recommender.recommend_activities()

    # 사용자에게 추천 운동 출력
    print(f"{user_name}님의 추천 운동:", recommendations)