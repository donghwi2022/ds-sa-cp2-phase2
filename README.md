# 내가 관심있는 의류 추천 서비스
## 1. 프로젝트 목표
  대학교 졸업 전까지는 옷에 관심이 없었는데, 졸업 이후 친구들과 사적 모임을 하게 되면서 친구들에게 패션에 대해 지적받으면서 옷에 관심이 생김. 하지만, 많은 옷 중에서 나에게 맞는 옷을 찾기 힘들고 친구들이 추천해주는 옷은 내가 마음에 들지 않는 경우가 종종 발생. <br>
  → 옷에 대한 정보를 바탕으로 나에게 맞는 옷을 추천해주는 시스템을 직접 만들어보기로 결정.
## 2. 프로젝트 진행 과정
  |구분|기간|활동|비고|
  |:---:|:---:|---|---|
  |사전 기획|1/31(화)|- 프로젝트 기획 및 데이터 확인||
  |데이터 전처리 및 <br> 시각화|2/1(수) ~ 2/2(목)|- 1차 데이터 전처리 진행 <br> - 다양한 시각화 진행||
  |데이터 전처리 추가 |2/3(금)|2차 데이터 전처리 진행|시각화 진행하면서 발견된 내용에 대해 추가적인 전처리|
  |모델링 및 성능 평가|2/6(월) ~ 2/10(금)|- baseline 모델 구현 <br> - 모델 구현(CB모델) <br> - 성능 평가|파일 경량화 작업 진행|
  |모듈화|2/13(월) ~ 2/14(화)|모델 모듈화|진행 내용을 python파일로 변경|
  |총 개발기간|1/31(화) ~ 2/14(화)(총 2주)|||
## 3. 데이터셋 설명
  - 데이터 요약 : 2016년 ~ 2022년까지 패션캠퍼스에서 수집한 고객들의 패션 구매 데이터
  - 데이터셋 주소 : https://www.kaggle.com/datasets/latifahhukma/fashion-campus?select=customer.csv
  - 사용한 데이터 파일
    : 아래의 3가지 파일을 하나의 csv파일로 만들어 사용(최초 용량 : 약 700MB)
    - customer.csv
    - product.csv
    - transaction_new.csv <br>
  - 컬럼 설명
    - created_at : 이벤트 발생시각
    - customer_id : 고객 id
    - session_id : 세션 id
    - payment_method : 결제 방식
    - payment_status : 결제 성공 여부
    - promo_amount : 할인 금액
    - promo_code : 프로모션 코드(할인쿠폰)
    - shipment_fee : 배송 비용
    - shipment_date_limit : 배송까지 최대 시각(언제까지는 도착할 것이다 느낌)
    - shipment_location_lat : 배송지역 위도
    - shipment_location_long : 배송지역 경도
    - total_amount : 총 비용
    - product_id : 상품 id
    - quantity : 주문 수량
    - item_price : 상품 가격
    - product_gender : 상품 타겟 성별
    - masterCategory : 최상위 분류
    - subCategory : 서브 분류
    - articleType : 상품 종류
    - baseColor : 기본 색상
    - season : 적합 계절
    - year : 상품 출시 년도
    - usage : 사용 방식(어느 복장인지)
    - productDisplayName : 상품 이름
    - customer_gender : 고객 성별
    - birthdate : 고객 생일
    - device_type : 디바이스 타입
    - device_id : 디바이스 id
    - device_version : 디바이스 버전
    - home_location_lat : 집 위도
    - home_location_long : 집 경도
    - home_location : 집 위치
    - first_join_date : 첫 가입 날짜
## 4. 프로젝트 진행 내용
  ### 1. 전처리
    - 중복 컬럼 drop
    - 특성을 추출하기 어렵다고 판단되는 내용 컬럼 drop(first_name, last_name 등)
    - 보안을 위해 hash값으로 처리된 데이터에 대해 시각적 편의를 위해 라벨링 진행
    - 시계엘 컬럼 길이 제한
  ### 2. 시각화
    - 전체 고객에 대한 분석
    - 전체 상품에 대한 분석
    - 사용 디바이스 종류 분석
    - 컬럼의 연도별 변화 분석(함수화하여 다양한 컬럼에 대해 분석할 수 있도록 작성)
    - 컬럼의 계절별 분석(함수화하여 다양한 컬럼에 대해 분석할 수 있도록 작성)
  ### 3. 추가 전처리
    - 불필요한 컬럼 drop
    - Category 컬럼 통합
    - 결측치 처리
    - 구매에 실패한 데이터 삭제
    - Parquet으로 파일 타입 변경(데이터 타입 변경시, 변경된 타입 저장)
  ### 4. 모델링
    - baseline 모델
      : 가장 빈도가 높은 상품 20개를 모든 고객에게 추천
    - 추천 모델
      - 상품의 정보를 바탕으로 CB모델을 통해 추천
      - OOM 문제를 해결하기 위해 코사인 유사도가 아닌 annoy 라이브러리를 사용
  ### 5. 성능평가
    - 20개의 상품을 추천
    - precision@k와 recall@k를 통해 성능평가
  ### 6. 모듈화
    1. 앞의 추천 모델을 python 파일로 작성 및 저장
    2. Colab에서 해당 python 파일을 불러와 추천 진행
## 5. 프로젝트 결과
  - 기준 모델의 성능(20개 추천 기준)
    - precision@k : 0.00013472549680026923
    - recall@k : 0.00036301053382020325
  - 추천 모델의 성능(20개 추천 기준)
    - precision@k : 0.0001613899180419891
    - recall@k : 0.0004927032935038315
  - 결과 요약
    : 2가지 성능평가 모두 기준모델보다 추천 모델이 점수가 높은 것을 확인할 수 있음
## 6. 한계점 및 향후 계획
  - 한계점
    - 시계열 정보를 활용하기 위해 함수를 작성해 보았으나 OOM 문제가 발생하여 시계열 정보를 활용하지 못함
    - 다양한 모델을 비교하고 싶었으나, 실력 부족으로 1가지 모델밖에 구현하지 못함
  - 향후 계획
    - 데이터만 활용하여 옷을 추천하는 것이 아닌 '학습'까지 활용한 추천 시스템을 모델링 해보고 싶음 <br>
      (참고자료- 딥러닝을 활용한 추천 모델링 예시)
      https://jalynne-kim.medium.com/%EC%B6%94%EC%B2%9C%EB%AA%A8%EB%8D%B8-%EC%9D%B4%EC%BB%A4%EB%A8%B8%EC%8A%A4-%EC%B6%94%EC%B2%9C%EB%AA%A8%EB%8D%B8%EB%A7%81-%EB%94%A5%EB%9F%AC%EB%8B%9D%EB%AA%A8%EB%8D%B8-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%ED%9A%8C%EA%B3%A0-d5017cb1335f
