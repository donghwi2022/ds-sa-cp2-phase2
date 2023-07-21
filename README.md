# 내가 관심있는 의류 추천 서비스
## 1. 프로젝트 목표
  대학교 졸업 전까지는 옷에 관심이 없었는데, 졸업 이후 친구들과 사적 모임을 하게 되면서 친구들에게 패션에 대해 지적받으면서 옷에 관심이 생김. <br>
  → Kaggle에서 얻은 옷 구매 이력 데이터를 바탕으로 의류 추천 모델을 모델링 해보기로 결정
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
  - 데이터 셋 : 2016년 ~ 2022년까지 패션캠퍼스에서 수집한 고객들의 패션 구매 데이터 (고객 정보, 상품 정보 등)
  - 데이터셋 주소 : https://www.kaggle.com/datasets/latifahhukma/fashion-campus?select=customer.csv
    ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/c02929ae-dd00-4065-95e9-71335522f946)
    - 총 40개 컬럼에 대하여 1,254,585개의 데이터
    - 이 중에서 33개의 컬럼만 사용
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
  - 예약 관련 컬럼
    1. booking_id가 같은 데이터는 session_id도 같기 때문에 booking_id 컬럼은 드랍하고 session_id는 라벨링 진행
  ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/ff7584e7-0e95-4830-9e57-97abe3332afd) 
  ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/779378e0-1743-448f-82b4-20afdb8d2710) 
      
  - 상품 정보 관련 컬럼
    1. id 컬럼은 product_id 컬럼과 같기 때문에 drop
    2. 상품 타겟 성별 컬럼은 "gender_x → product_gender"로 변경
    3. 기본 색상 컬럼은 "baseColour → baseColor"로 변경
  ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/f28e67e5-e72e-49ac-a908-00e62dff2c40) 

  - 고객 정보 관련 컬럼
    1. 고객 이름 ~ 고객 이메일에 해당하는 컬럼은 앞의 customer_id로 대체 가능하므로 모두 drop
    2. "gender_y → customer_gender"로 컬럼명 변경
  ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/ad30f2ab-c0fa-434e-aedf-b3fcaa238624) 

  - 기기 정보 관련 컬럼
    1. device_id 컬럼에 라벨 인코딩 적용
  ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/ecd74272-8f01-4485-bb94-0cb1c7744b6e)
    
  - 고객 집 위치 정보 관련 컬럼
    1. home_country 컬럼의 값이 인도네시아밖에 존재하지 않으므로 drop
  ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/6bc0c0d9-e9c4-471e-b41d-80ce1523c8a8)

  - first_join_date 컬럼 및 시계열 컬럼
    1. created_at, shipment_date_limit : 초 단위까지만 나오도록 길이 제한
  ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/ed970f58-e591-4dc4-8e8b-fc3e0de882e9)

  ### 2. 시각화
  - 구매 성공-실패 비율 <br>
     ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/72a9465b-c4c8-4e5a-a707-b123bc26098b) <br>
    : 전체 데이터 중에서 구매에 실패한 데이터는 고객이 입는 옷이라고 판단하기 어렵기 때문에 추가 전처리에서 제거 진행 <br>
    
  ### 3. 추가 전처리
  - 미사용 컬럼 제거 및 병합 <br>
  ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/147ee7bb-6c6a-457a-a9e0-9fb68e524c2d)

  - 결측치 처리 <br>
  ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/11b2fd56-9d19-4231-9020-a824e9130eed)
    - baseColor : 'Unknown'으로 결측치 채움
    - promo_code : 'No'로 결측치 채움
    - usage : 'Unknown'으로 결측치 채움
    - productDisplayName : 'Unknown'으로 결측치 채움
    - season : 'Unknown'으로 결측치 채움
    - year : 결측치에 해당하는 행 삭제

  - 구매에 실패한 데이터 삭제후, 'payment_status' 컬럼 삭제 <br>
  ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/42f8aec3-028c-4204-8873-aa98d1943a80)

  - 데이터 타입 변경 (메모리 문제 해결 방안) <br>
  ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/4bf0bedf-e2fc-4d8f-8663-a11dc18b00b2)

  - Parquet으로 파일 타입 변경(변경된 데이터 타입 유지) <br>
  ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/fb05e569-9af6-47b3-8696-63e75a41ccce)

  ### 4. 모델링
  - 학습 데이터와 테스트 데이터 분리 <br>
    ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/714dfddf-1027-4765-b05e-c5569b433e7f) <br>
    : 학습 데이터와 테스트 데이터를 4:1의 비율로 분리 <br>
    <br>
  - baseline 모델 <br>
      ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/ac50877f-9cde-4309-bfe6-b5b2df8ee33b) <br>
    : 가장 빈도가 높은 상품 20개를 모든 고객에게 추천 <br>
  - annoy 모델(벡터 유사도)을 사용한 추천 <br>
    ① 사용할 컬럼 선택 <br>
        ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/a82afacb-5f3e-4596-83e6-f6685e23d403) <br>
        ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/dc937654-cf05-46be-b242-63fd3abf7db9) <br>
      : 여러 가지의 컬럼 중, product_gender, baseColor, season, year, usage, Category의 총 6개 컬럼을 사용 <br>
    ② 벡터 유사도를 계산하기 위해 묶기 <br>
        ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/9bc09605-725d-4aaf-b9bb-901de512628a) <br>
        ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/fe529d3d-e5eb-463f-ac8d-04f5d9c9baae) <br>
      : 벡터 유사도를 계산하기 위해 위의 컬럼들을 'features'라는 컬럼으로 통합 <br>
    ③ 벡터화 진행 <br>
        ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/ea89e138-04d6-4928-8f79-f09a56935bd3) <br>
      : 모든 문서에서 자주 등장하는 단어에 대해서 패널티를 주는 tf-idf 벡터화를 사용 <br>
    ④ 모델 초기화 <br>
        ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/d6c275f9-c85c-48e3-8d79-185e6af8c532) <br>
      : 두 벡터 사이의 각도가 작을 때 코사인 유사도에서 큰 차이를 보이지 않는 문제를 해결한 angular를 metric으로 사용
    ⑤ 모델 구축 <br>
        ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/562e2258-4a47-4e8b-a0e2-3cd68ad809f0) <br>
      : 트리가 깊을수록 정확도가 올라가지만 빠른 결과 확인을 위해 깊이가 5인 모델을 구축
    ⑥ 추천 진행 <br>
        ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/a8b47acc-14ff-4ae2-bc31-32b18d21b4d5) <br>
      : 고객 id를 입력받아 추천을 진행하는 함수를 만들고 동작 확인을 위해 고객 id가 89369인 고객으로 테스트 진행 <br>
    ⑦ 추천 결과(id가 89369인 고객에 대한 추천 진행 결과) <br>
        ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/e08ce65a-0138-4ecc-b4e9-1a09c28b659e) <br>
      : 해당 고객에 대하여 추천하는 상품인 20개의 상품 정보를 출력하는 것을 확인할 수 있음 <br>

  ### 5. 성능평가
  - 모든 고객에 대하여 20개의 상품 추천을 진행
    - baseline 모델 : 모든 고객에게 빈도가 높은 상품 20개를 동일하게 추천
    - annoy 모델 : 각각의 고객에게 벡터 유사도가 높은 상품 20개를 추천
  - precision@k와 recall@k를 통해 성능평가(성능평가 결과는 프로젝트 결과에 표기) <br>
  ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/ba6e1b04-8f30-4b63-9940-3d0655655a4c)
    - precision@k : 추천한 상품 중에서 실제 구매 이력이 있는 상품의 비율
    - recall@k : 실제 구매 이력이 있는 상품 중에서 추천한 상품의 비율

  ### 6. 모듈화
  1. 앞의 추천 모델을 python 파일로 작성 및 저장 <br>
  ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/4dadf6f5-b305-4cc8-b072-49cc674f2bcf) <br>
    : Visual Studio를 활용하여 구매 이력 데이터를 가져와 추천을 진행하기까지 함수를 하나의 Python 파일로 작성 <br>
  2. 파일 저장 위치로 이동 <br>
  ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/4f34c2e2-5f53-493a-9609-86d257b5542f) <br>
    : 해당 Python 파일을 활용하기 위해 저장된 위치로 이동 <br>
  3. Colab에서 해당 python 파일을 불러와 추천 진행 <br>
  ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/bad73ef9-0a28-4b5f-9fdc-e75585bc73be) <br>
  ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/503b5897-1f81-42f9-befc-e133bdc59c0b) <br>
    : Colab에서 해당 python 파일을 불러와 추천 함수까지 정상적으로 동작하는 것을 확인 <br>
## 5. 프로젝트 결과
  - baseline 모델의 성능 : 모든 고객에게 빈도가 높은 상품 20개를 동일하게 추천한 결과의 평균
    - precision@k : 0.00013472549680026923
    - recall@k : 0.00036301053382020325
  - 추천 모델의 성능 : 각각의 고객에게 벡터 유사도가 높은 상품 20개를 추천한 결과의 평균
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
      (참고자료- 딥러닝을 활용한 추천 모델링 예시) <br>
      https://jalynne-kim.medium.com/%EC%B6%94%EC%B2%9C%EB%AA%A8%EB%8D%B8-%EC%9D%B4%EC%BB%A4%EB%A8%B8%EC%8A%A4-%EC%B6%94%EC%B2%9C%EB%AA%A8%EB%8D%B8%EB%A7%81-%EB%94%A5%EB%9F%AC%EB%8B%9D%EB%AA%A8%EB%8D%B8-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%ED%9A%8C%EA%B3%A0-d5017cb1335f
