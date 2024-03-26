# MBTI_ActivityRecommender
학교 캡스톤으로 MBTI 별 운동 추천 알고리즘을 구현했습니다.

# activities information
운동 정보는 다음과 같이 각 운동을 key로 두고 운동에 따른 MBTI값을 뇌피셜이지만 추가 해주었습니다.
```json
{
    "복싱" : [0.72, 0.24, 0.64, 0.76],
    "피겨" : [0.20, 0.67, 0.34, 0.78],
    "배드민턴" : [0.82, 0.37, 0.22, 0.65]
}
```

# user information
유저 정보는 다음과 같습니다. MBTI 특성분류 4가지를 Key값으로 작성하였습니다.
```json
{
    "user" : "홍길동",
    "I" : 0.68,
    "S" : 0.80,
    "T" : 0.72,
    "P" : 0.56
}
```

# MBTI format
MBTI의 분류는 16가지 입니다. 각 MBTI 별로 코드를 작성하는 것은 어렵다고 판단해 하나의 MBTI를 기준으로 잡고 다른 MBTI는 1에서 빼는 식으로 진행했습니다. MBTI가 각 분류당 2차원으로 나눠지기에 가능했습니다.
```python
mbti_vector = [
    1 - input_json.get('I', 0) if 'I' in input_json else input_json.get('E', 0),
    1 - input_json.get('N', 0) if 'N' in input_json else input_json.get('S', 0),
    1 - input_json.get('T', 0) if 'T' in input_json else input_json.get('F', 0),
    1 - input_json.get('J', 0) if 'J' in input_json else input_json.get('P', 0)
]
```

# 벡터 스케일링 적용
코사인 유사도는 -1부터 1 사이값을 가집니다. 그러나 MBTI 벡터들은 0~1사이의 양수 값을 가지기 때문에 유사도를 구할 경우 양수값이 나올 수 밖에 없습니다.<br>
때문에 4가지의 각 MBTI벡터와 운동정보 벡터들을 -1과 1로 범위를 늘리는 스케일링을 해주었습니다. 스케일링 공식은 아래와 같습니다. <br>
```python
def normalize_vector(vector):
    """벡터의 각 요소를 -1과 1 사이의 값으로 정규화."""
    return [2 * x - 1 for x in vector]
```
<p align="center">
  <img src="https://github.com/StatisticsFox/MBTI_ActivityRecommender/assets/92065443/984b45ec-402b-4404-b2d3-622b658dfb8c" width="10%" height="auto" />
</p>

# 추천 알고리즘
알고리즘은 코사인 유사도를 계산하는 방식으로 구현했습니다. <br>
유저가 본인의 MBTI수치를 입력하면 운동 MBTI 수치와 비교하여 0.5이상인 운동을 유저에게 추천 해줍니다.<br>
어떤 수치 이상을 알려줄지 상위 5개의 운동을 추천해줄지는 팀원과 상의를 통해 그리고 요구사항 분석을 진행 해서 더 디밸롭할 예정입니다.

## 코사인 유사도란?
-1부터 1의 값을 가지며 1에 가까울수록 두 벡터가 비슷한 성질을 지닌다고 판단합니다.
수식은 다음과 같습니다.<br>
## $$cos(\Theta ) = \frac{A\cdot B}{\left \|| A \right \||\left \|| B \right \||}$$

 
