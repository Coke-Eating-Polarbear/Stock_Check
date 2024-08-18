**What about**
---
1. **main.py**
   - 용도 : Excel 형태로 정리되어있는 파일을 가져와 그래프 형태로 출력
   - 추후 개선점 : 원하는 그래프의 형태를 선택이 아닌 정규식을 이용하여 문장형태로 입력하여 출력하기 
2. **SQL.py**
   - 용도 : 재무제표를 이용하여 출력할수있는 모든 데이터를 출력.
   - 추후 개선점 : main.py와 같은 graph그리기를 사용할 예정, 읽어온 재무제표들을 MySQL안에 넣기, 만약 SQL안에 주식의 데이터가 있다면 지금의 재무제표와 비교하여 다를경우 추가적으로 출력하는 기능
3. **function/cal_fin.py**
   - 용도 : 재무제표의 모든 데이터를 계산하는데 사용하는 함수들의 집합
   - 추후 개선점 : 재무제표를 이용하여 얻을수있는 정보가 있다면 그것도 포함하여 출력시키는데 사용할 예정
4. **function/graph.py**
   - 용도 : main.py에서 그래프를 그리는데 사용하는 함수들의 집합.
   - 추후 개선점 : main.py와 SQL.py에서 입력받은 원하는 형태의 그래프를 출력시키는 정규식을 추가할 예정.

**Why I made it**
---
우리 FISA에서 교육을 들으면서 배웠던것들을 모두 사용하기 위해서 만들기 시작하였습니다. 주제 선정에는 같이 수업을 듣는 동기의 제안으로 시작하였습니다.
현재의 프로토 타입으로 추후에 사용을 할수있게 될정도로 업그레이드가 된다면 이것을 통해서 주식을 제대로 해보고 싶었습니다.

제작자 : 김명준
프로토타입 제작 완료일 2024-08-18
