# 📝 Git 명령어 요약 정리 (Cheat Sheet)

## 1. 깃 시스템 및 초기 설정 관리 (System & Config)

| 기능 | 명령어 | 설명 |
| :--- | :--- | :--- |
| **저장소 초기화 및 생성** | `$ git init` | 현재 디렉토리를 **Git 저장소로 생성**. |
| | `$ git init basic` | 하부 폴더를 생성하고 Git 저장소로 만듦. |
| **환경 설정** | `$ git config --global user.name <이름>` | **사용자 이름** 설정. |
| | `$ git config --global user.email <이메일>` | **사용자 전자메일** 설정. |
| | `$ git config --global init.defaultBranch main` | **기본 브랜치 이름** 설정. |
| | `$ git config --list` | 설정 변수 및 값 확인. |
| | `$ git config --global alias.<별칭> ‘<원명령어>’` | 자주 사용하는 Git 명령어의 **별칭 생성**. |
| **정보 확인** | `$ git --version` | **Git 버전** 확인. |

---

## 2. 버전 관리 흐름 (Working Flow: Stage & Commit)

| 기능 | 명령어 | 설명 |
| :--- | :--- | :--- |
| **상태 확인 (Status)** | `$ git status` | 현재 상태 표시. |
| | `$ git status [--short \| -s]` | 현재 상태를 **간단히 표시**. |
| **추가/스테이징 (Add)** | `$ git add <file>` | 파일을 **작업 디렉토리(WD)**에서 **스테이징 영역(Index)으로 이동(복사)**. |
| **커밋 (Commit)** | `$ git commit -m ‘message’` | 스테이징 영역의 변경 사항을 **Git 저장소에 기록/저장**. |
| | `$ git commit -a -m ‘message’` | **이미 추적된 파일의 수정**에 대해 **추가(add)와 커밋을 함께 실행**. |

---

## 3. 이력 확인 및 시간 여행 (Log & Navigation)

| 기능 | 명령어 | 설명 |
| :--- | :--- | :--- |
| **로그 이력 확인** | `$ git log` | **로그 이력 정보**를 표시 (최근 커밋부터). |
| | `$ git log --oneline` | 로그 이력을 **한 줄로 간략히** 표시. |
| | `$ git log --graph` | **문자 그림**으로 로그 이력을 그리기. |
| | `$ git log --all` | **모든 브랜치**의 로그 이력 표시. |
| | `$ git show [commitID]` | 지정한 커밋 ID의 **상세 정보(Diff 포함)** 표시. |
| **과거 버전 이동** | `$ git checkout HEAD~` | **HEAD 이전 커밋**으로 이동 (**분리된 HEAD 상태**). |
| | `$ git switch -d [이전커밋]` | 이전 커밋으로 이동 (**분리된 HEAD 상태로 전환**). |
| | `$ git switch main` | **main 브랜치의 최신 커밋**으로 돌아오기. |
| | `$ git switch -` | **이전 checkout 위치** 또는 **이전 브랜치**로 돌아오기. |

---

## 4. 파일 비교, 삭제 및 복원 (Diff, Remove & Restore)

| 기능 | 명령어 | 비교 대상 |
| :--- | :--- | :--- |
| **파일 비교 (Diff)** | `$ git diff` | **스테이징 영역 기준**으로 **작업 디렉토리** 파일 비교. ($\text{Index} \leftrightarrow \text{WD}$) |
| | `$ git diff --staged` | **깃 저장소 기준**으로 **스테이징 영역** 파일 비교. ($\text{HEAD} \leftrightarrow \text{Index}$) |
| | `$ git diff HEAD` | **깃 저장소 기준**으로 **작업 디렉토리** 파일 비교. ($\text{HEAD} \leftrightarrow \text{WD}$) |
| **파일 삭제 (Remove)** | `$ git rm [file]` | **WD와 SA에서 파일 삭제** (다음 커밋에 삭제 예약). |
| | `$ git rm --cached [file]` | **SA에서만 파일 삭제** (WD 파일 유지). |
| **파일 복원 (Restore)** | `$ git restore [file]` | **스테이징 영역**의 상태를 **작업 디렉토리에 복원**. (WD의 변경 취소) |
| | `$ git restore --staged [file]` | **깃 저장소** 상태를 **스테이징 영역에 복원**. (SA의 변경 취소) |

---

## 5. 브랜치 및 태그 관리 (Branch & Tag)

| 기능 | 명령어 | 설명 |
| :--- | :--- | :--- |
| **브랜치 생성 및 이동** | `$ git branch <new-branch>` | 새 브랜치 생성 (**HEAD 이동 없음**). |
| | `$ git switch -c [newBranch]` | 브랜치 **생성 후 HEAD 이동**. |
| | `$ git branch` | **브랜치 목록** 표시 (\*은 현재 브랜치). |
| | `$ git branch -d [branchName]` | **병합된 브랜치** 삭제. |
| **태그 관리** | `$ git tag v1.0.1` | **일반(가벼운) 태그** 생성. |
| | `$ git tag –a v1.0.0 –m ‘message’` | **주석 태그** 생성 (메시지, 작성자 정보 포함). |
| | `$ git tag` | **태그 목록** 보기. |
| | `$ git show v1.0.0` | **특정 태그의 자세한 정보** 확인. |

---

## 6. 원격 저장소 연동 (Remote Synchronization)

| 기능 | 명령어 | 설명 |
| :--- | :--- | :--- |
| **저장소 복제 및 관리** | `$ git clone [주소]` | 원격 저장소를 **지역 저장소에 복제**. |
| | `$ git remote -v` | **원격 저장소 주소와 별칭** 목록 표시 (기본값: `origin`). |
| **데이터 송수신** | `$ git push <별칭명> <브랜치명>` | 지역 저장소의 변경 이력을 **원격 저장소로 전송/올리기**. |
| | `$ git pull` | 원격 저장소의 수정을 지역 저장소에 반영 (**fetch + merge**). |
| | `$ git fetch <remote>` | 원격 저장소 정보를 가져오지만 **병합은 미수행**. |
| | `$ git merge origin/main` | `fetch` 명령으로 가져온 내용을 **로컬 저장소의 내용과 병합**. |
