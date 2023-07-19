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
  1. 고객 분석
     1. 상위 10명의 거래량 <br>
     ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/e5de8e4c-962a-41ca-8225-462a742506d8) <br>
     2. 고객의 성별 비율 <br>
     ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/74abe73e-d96b-4143-914e-2a14afd3015a) <br>
     3. transaction 기준 연령대 분포 <br>
     ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/61114dd4-bd20-4f6a-b805-d4b149bac5be) <br>
     4. 고객의 연도별 패션 카테고리 변화 <br>
     ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/08278a4a-7688-485e-b71e-ec1997a20b0a) <br>
  
  3. 상품 분석
     1. 상품의 타겟 성별 비율 <br>
     ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/7a97c30e-8ba2-426e-b6a6-44adcd45c0eb) <br>
     2. 상품의 분류별 비율 <br>
     ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/a8e6f9ea-104f-473c-9dfc-bd47275d61fa) <br>
     3. 상품의 사용 복장 <br>
     ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/31ec08d6-2a01-4548-8d70-540f9afd0093) <br>
     4. 고객들이 많이 찾은 계절 복장 <br>
     ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/dba9ec24-3395-4075-a7fa-b96b550e6e6d) <br>

  4. 컬럼의 연도별 변화
     1. 연도별 디바이스 타입 변화 <br>
     ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/6d0163f5-ced0-4432-90f5-ef500c168483) <br>
     2. 연도별 결제 방식 변화 <br>
     ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/7b80f1d3-f494-450d-a68d-6f6a2af269f8) <br>

  5. 컬럼의 계절별 변화
     1. 계절별 결제 방식 <br>
     ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/046c3b44-43fe-4b27-96d4-7f160e3ec204) <br>
     2. 계절별 상품 masterCategory <br>
     ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/09f10447-caac-4241-8715-eaa3c1536ea7) <br>

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
  - baseline 모델
    : 가장 빈도가 높은 상품 20개를 모든 고객에게 추천 <br>
      ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/ac50877f-9cde-4309-bfe6-b5b2df8ee33b) <br>

  - annoy 모델(벡터 유사도)을 사용한 추천 <br>
    ① 사용할 특성 선택 <br>
      &nbsp; ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/a82afacb-5f3e-4596-83e6-f6685e23d403) <br>
      &nbsp; ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/ecbbf567-ee57-487c-9900-bca1074ca4b2) <br>
    
    ② 벡터 유사도를 계산하기 위해 특성 묶기 <br>
      &nbsp; ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/9bc09605-725d-4aaf-b9bb-901de512628a) <br>
      &nbsp; ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/fe529d3d-e5eb-463f-ac8d-04f5d9c9baae) <br>
    
    ③ 벡터화 진행 <br>
      &nbsp; ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/ea89e138-04d6-4928-8f79-f09a56935bd3) <br>
    
    ④ 모델 초기화 <br>
      &nbsp; ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/d6c275f9-c85c-48e3-8d79-185e6af8c532) <br>
    
    ⑤ 모델 구축 <br>
      &nbsp; ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/562e2258-4a47-4e8b-a0e2-3cd68ad809f0) <br>
    
    ⑥ 추천 진행 <br>
      &nbsp; ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/b3ada977-32de-4aba-9313-59c1281ec08d) <br>
    
    ⑦ 추천 결과 <br>
      &nbsp; ![image](https://github.com/donghwi2022/ds-sa-cp2-phase2/assets/73475048/e08ce65a-0138-4ecc-b4e9-1a09c28b659e) <br>

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
      (참고자료- 딥러닝을 활용한 추천 모델링 예시) <br>
      https://jalynne-kim.medium.com/%EC%B6%94%EC%B2%9C%EB%AA%A8%EB%8D%B8-%EC%9D%B4%EC%BB%A4%EB%A8%B8%EC%8A%A4-%EC%B6%94%EC%B2%9C%EB%AA%A8%EB%8D%B8%EB%A7%81-%EB%94%A5%EB%9F%AC%EB%8B%9D%EB%AA%A8%EB%8D%B8-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%ED%9A%8C%EA%B3%A0-d5017cb1335f
