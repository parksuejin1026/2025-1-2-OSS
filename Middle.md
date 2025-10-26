# 📝 Git 명령어 요약 정리 (기능 및 예시 포함)

## 1. 깃 시스템 및 초기 설정 관리 (System & Config)

| 기능 분류 | 명령어 | 설명 | 예시 |
| :--- | :--- | :--- | :--- |
| **저장소 생성** | `$ git init` | 현재 디렉토리를 **새로운 Git 저장소로 초기화**합니다. | `$ git init` |
| | `$ git init basic` | `basic`이라는 **하위 디렉토리를 생성하고 Git 저장소로 초기화**합니다. | `$ git init my_project` |
| **사용자 설정** | `$ git config --global user.name <이름>` | **커밋에 기록될 사용자 이름**을 전역적으로 설정합니다. | `$ git config --global user.name "Gildong Hong"` |
| | `$ git config --global user.email <이메일>` | **커밋에 기록될 사용자 이메일**을 전역적으로 설정합니다. | `$ git config --global user.email "gd.hong@example.com"` |
| **별칭 생성** | `$ git config --global alias.<별칭> ‘<원명령어>’` | 자주 사용하는 명령어에 대한 **별칭(단축어)**을 생성합니다. | `$ git config --global alias.st 'status -s'` |
| **정보 확인** | `$ git --version` | 설치된 **Git의 버전**을 확인합니다. | `$ git --version` |

---

## 2. 버전 관리 흐름 (Working Flow: Stage & Commit)

| 기능 분류 | 명령어 | 설명 | 예시 |
| :--- | :--- | :--- | :--- |
| **상태 확인** | `$ git status` | 현재 **파일 상태를 상세히** 표시합니다. | `$ git status` |
| | `$ git status -s` | 현재 파일 상태를 **두 문자 코드**로 **간결하게 요약**하여 표시합니다. | `$ git status -s` |
| **스테이징 (Add)** | `$ git add <file>` | **WD의 변경 사항을 SA로 이동**하여 다음 커밋에 포함되도록 준비합니다. | `$ git add index.html` |
| | `$ git add .` | **현재 디렉토리의 모든 변경 사항**을 스테이징합니다. | `$ git add .` |
| **커밋 (Commit)** | `$ git commit -m ‘message’` | **SA에 준비된 변경 사항**을 **깃 저장소에 기록/저장**합니다. | `$ git commit -m "feat: 로그인 기능 추가"` |
| | `$ git commit -a -m ‘message’` | **추적 파일의 수정**에 대해 **add와 commit을 함께** 실행합니다. | `$ git commit -a -m "fix: 오타 수정"` |

---

## 3. 이력 확인 및 시간 여행 (Log & Navigation)

| 기능 분류 | 명령어 | 설명 | 예시 |
| :--- | :--- | :--- | :--- |
| **로그 기본 확인** | `$ git log` | **커밋 이력**을 최근 커밋부터 상세히 표시합니다. | `$ git log` |
| | `$ git log --oneline` | 커밋 이력을 **한 줄로 간략히** 표시합니다. | `$ git log --oneline` |
| | `$ git log --graph` | **브랜치 및 병합 관계**를 **문자 그래프로 시각화**하여 표시합니다. | `$ git log --oneline --graph` |
| **특정 커밋 확인** | `$ git show [commitID]` | **지정한 커밋의 정보와 파일 변경 내용**을 자세히 표시합니다. | `$ git show a1b2c3d` |
| **과거 버전 이동** | `$ git switch -d [이전커밋]` | **지정한 커밋 상태**로 **HEAD를 분리하여** 이동합니다. | `$ git switch -d HEAD~2` |
| | `$ git switch main` | **main 브랜치의 최신 커밋**으로 돌아옵니다. | `$ git switch main` |
| | `$ git switch -` | **직전에 작업하던 위치**로 빠르게 전환합니다. | `$ git switch -` |

---

## 4. 파일 비교, 삭제 및 복원 (Diff, Remove & Restore)

| 기능 분류 | 명령어 | 설명 | 예시 |
| :--- | :--- | :--- | :--- |
| **WD 변경 비교** | `$ git diff` | **스테이징되지 않은(unstaged) 내용**을 비교합니다. | `$ git diff` |
| **SA 변경 비교** | `$ git diff --staged` | **커밋 예정인(staged) 내용**을 비교합니다. | `$ git diff --staged` |
| **전체 변경 비교** | `$ git diff HEAD` | **마지막 커밋 대비 WD의 모든 변경점**을 비교합니다. | `$ git diff HEAD` |
| **Git 파일 삭제** | `$ git rm [file]` | **WD와 SA에서 파일 삭제** 후, 삭제를 커밋에 예약합니다. | `$ git rm old_file.txt` |
| | `$ git rm --cached [file]` | **SA에서만 추적을 중단**하고, WD 파일은 유지합니다. | `$ git rm --cached .env` |
| **WD 변경 복원** | `$ git restore [file]` | **SA의 상태**로 **WD 파일의 변경 사항을 되돌립니다**. | `$ git restore script.js` |
| **SA 변경 복원** | `$ git restore --staged [file]` | **깃 저장소(HEAD) 상태**로 **SA의 파일 상태를 되돌립니다**. | `$ git restore --staged index.html` |

---

## 5. 브랜치 및 태그 관리 (Branch & Tag)

| 기능 분류 | 명령어 | 설명 | 예시 |
| :--- | :--- | :--- | :--- |
| **브랜치 생성** | `$ git branch <new-branch>` | **새 브랜치를 생성**만 합니다. | `$ git branch feature/login` |
| **브랜치 생성/이동** | `$ git switch -c [newBranch]` | 새 브랜치를 생성하고 **바로 해당 브랜치로 전환**합니다. | `$ git switch -c feature/auth` |
| **브랜치 목록** | `$ git branch` | **로컬 브랜치 목록**을 표시합니다. | `$ git branch` |
| **브랜치 삭제** | `$ git branch -d [branchName]` | **병합이 완료된 브랜치**를 삭제합니다. | `$ git branch -d feature/old` |
| **일반 태그 생성** | `$ git tag v1.0.1` | 특정 커밋에 **가벼운(Lightweight) 태그**를 생성합니다. | `$ git tag v1.0.0` |
| **주석 태그 생성** | `$ git tag –a v1.0.0 –m ‘message’` | **주석(Annotation)과 작성자 정보**를 포함하는 태그를 생성합니다. | `$ git tag -a v1.0.0 -m "Release v1.0"` |
| **태그 목록** | `$ git tag` | **모든 태그 목록**을 표시합니다. | `$ git tag` |

---

## 6. 원격 저장소 연동 (Remote Synchronization)

| 기능 분류 | 명령어 | 설명 | 예시 |
| :--- | :--- | :--- | :--- |
| **저장소 복제** | `$ git clone [주소]` | 원격 저장소를 **지역 저장소에 복제**합니다. | `$ git clone https://github.com/repo/project.git` |
| **원격 정보 확인** | `$ git remote -v` | **연결된 원격 저장소의 주소와 별칭** 목록을 표시합니다. | `$ git remote -v` |
| **데이터 전송** | `$ git push <별칭명> <브랜치명>` | 지역 저장소의 커밋 이력을 **원격 저장소로 전송**합니다. | `$ git push origin main` |
| **데이터 수신** | `$ git pull` | 원격 저장소의 변경 내용을 가져와 **자동으로 병합**합니다. | `$ git pull` |
| | `$ git fetch <remote>` | 원격 저장소 정보를 가져오지만 **병합은 하지 않습니다**. | `$ git fetch origin` |
| **가져온 내용 병합** | `$ git merge origin/main` | `fetch`로 가져온 원격 브랜치를 **현재 로컬 브랜치와 병합**합니다. | `$ git merge origin/main` |
