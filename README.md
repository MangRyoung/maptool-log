# 맵툴 로그 정리기

MapTool 채팅 로그(HTML · 텍스트)를 읽기 좋은 세션 로그로 정리하는 한 장짜리 웹 페이지. 브라우저 안에서만 돌고, 로그·이미지는 그 브라우저(IndexedDB)에 남는다.

- 로그 파일 여러 개를 이어 보기 · 편집 · 모두 바꾸기
- 캠페인 파일(.cmpgn)·에셋 폴더로 토큰 이미지 자동 연결, BGM 파일 연결
- 표시 옵션(잡담 · 귓속말 · 주사위 식 · 시간 · 연속 발언 묶기 · 시스템), HTML/텍스트 내보내기

## 오레마스 연동
「오레마스 방 불러오기」 칸에 방 링크(`…/oremas/#r=방ID`)나 방 ID 를 넣으면 그 방의 로그를 읽어 온다.
- 대사 · *지문* · 주사위 · 배틀 카드(지령 · 고유 · 포텐셜 … 효과 본문 포함) · 시스템 줄을 옮긴다. 휴대폰 문자는 고르면 넣는다. 귓속말은 서버가 공개하지 않아 빠진다.
- 화자 초상은 방의 로스터(트레이너 · 포켓몬) · 관계도 · 스탠딩 그림에서 가져와 토큰 이미지로 잇는다.
- 오레마스의 「💾 로그 → 정리기에서 열기」는 `?oremas=방ID` 로 이 페이지를 열어 바로 불러온다.
- **오레마스에서 내보낸 파일**도 「로그 파일 추가」 · 끌어 놓기 · 붙여넣기로 넣을 수 있다. HTML 은 안에 든 원본 데이터(`<script id="oremas-log">`)로 초상 · 주사위 · 배틀 카드를 그대로 살리고, 그 데이터가 없는 옛 파일은 말풍선 꼴을 읽는다. TXT 는 날짜를 떼고 원래 파서로 읽는다.
- 오레마스에서 올린 그림은 「[그림]」 대신 그 자리에 그림으로 보이고, HTML 복사에도 들어간다.
- 읽기 전용. 오레마스와 같은 Supabase 프로젝트의 공개 키로 `om_rooms` · `om_state` · `om_log` 를 읽는다.

## 파일
- `src/original.html` — 정리기 원본(그대로 둔다)
- `oremas-addon.html` — 오레마스 연동 덧붙임(패널 + 스크립트)
- `build.py` — 두 파일을 합쳐 `index.html` 을 만든다. 원본이 바뀌면 `src/original.html` 만 갈아 끼우고 `python build.py`.
- `index.html` — GitHub Pages 가 내보내는 페이지

## 올리기
GitHub Desktop → File › Add local repository → 이 폴더 → Publish repository(`maptool-log`, Public) → 저장소 Settings › Pages › Branch `main` / root.
주소: https://mangryoung.github.io/maptool-log/
