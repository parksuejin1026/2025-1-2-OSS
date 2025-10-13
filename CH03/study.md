# 📚 Git 핵심 기능 요약 (3장 & 4장) - GitHub 정리용

## 📌 3장: 커밋, 로그 이력 및 과거 버전 이동 (Commit, Log History, and Time Travel)

### 1. 깃의 3가지 영역 (Three States) 및 버전 관리 프로세스

[cite_start]Git은 파일을 세 가지 상태(영역)로 구분하여 관리합니다[cite: 7, 9]. [cite_start]`add` 명령과 `commit` 명령을 통해 버전 관리를 진행합니다[cite: 7].

| 영역 | 설명 | 상태 | 주요 명령 |
| :--- | :--- | :--- | :--- |
| **작업 디렉토리** (Working Directory) | [cite_start]실제 파일이 존재하는 폴더[cite: 7, 9]. | [cite_start]Untracked (Git 관리 X) 또는 Modified (수정됨)[cite: 7, 9]. | `echo`, `touch`, `rm` |
| **스테이징 영역** (Staging Area/Index) | [cite_start]다음 커밋에 포함할 변경 사항을 준비하는 임시 공간[cite: 7, 9]. | [cite_start]Staged (커밋 준비 완료)[cite: 7, 9]. | `git add` |
| **깃 저장소** (Git Repository) | [cite_start]커밋된 파일의 모든 버전 이력(`.git` 폴더 내부)[cite: 7, 9]. | [cite_start]Committed (버전 저장 완료)[cite: 7, 9]. | `git commit` |

### 2. 커밋 및 로그 확인 명령어

버전 관리를 위해 변경 사항을 저장하고(커밋), 그 이력을 확인하는(로그) 핵심 명령어입니다.

| 명령 | 설명 |
| :--- | :--- |
| `\$ git status` | [cite_start]현재 작업 디렉토리와 스테이징 영역의 **상태**를 확인합니다[cite: 7]. |
| `\$ git add [file]` | [cite_start]파일을 **스테이징 영역**에 추가하여 다음 커밋에 포함되도록 준비합니다[cite: 7, 9]. |
| `\$ git commit -m "[메시지]"` | [cite_start]스테이징 영역의 내용을 **깃 저장소**에 영구적으로 저장합니다[cite: 7, 9]. |
| `\$ git log` | [cite_start]저장된 **모든 커밋 이력**을 상세하게 확인합니다[cite: 7, 8, 9]. |
| `\$ git log --oneline` | [cite_start]커밋 ID와 메시지를 **한 줄**로 간결하게 요약하여 확인합니다[cite: 7, 8, 9]. |
| `\$ git log --graph` | [cite_start]브랜치와 커밋 이력을 **그래프** 형태로 확인합니다[cite: 7, 8]. |
| `\$ git show [CID]` | [cite_start]특정 커밋(Commit ID)의 **상세 정보와 변경 내용(diff)**을 확인합니다[cite: 8, 9]. |

### 3. 과거 버전 참조 및 이동 (시간 여행)

[cite_start]**HEAD**는 현재 브랜치의 최신 커밋을 가리키는 포인터입니다[cite: 8, 9]. 이를 사용하여 과거 버전으로 돌아가거나 참조할 수 있습니다.

| 참조 (Commit ID 대신 사용) | 의미 |
| :--- | :--- |
| **HEAD** | [cite_start]현재 작업 중인 가장 최신 커밋[cite: 8]. |
| **HEAD~** 또는 **HEAD^** | [cite_start]**하나 전** 커밋[cite: 8, 9]. |
| **HEAD~n** (n은 숫자) | [cite_start]**n번째 전** 커밋 (예: `HEAD~2`는 두 개 전)[cite: 8, 9]. |
| **[Commit ID]** | [cite_start]40자리 해시값 또는 앞 7자리로 특정 커밋을 지칭[cite: 8, 9]. |

| 명령 | 설명 |
| :--- | :--- |
| `\$ git checkout [CID]` | [cite_start]**특정 커밋** 상태로 작업 디렉토리를 이동합니다[cite: 8, 9]. |
| `\$ git checkout HEAD~` | [cite_start]**하나 전 커밋** 상태로 작업 디렉토리를 이동합니다[cite: 8]. |
| `\$ git checkout main` | [cite_start]**최신 버전(main 브랜치)**으로 복귀합니다[cite: 8, 9]. |

---

## 🔪 4장: 파일 비교, 삭제 및 복원 (Diff, RM, Restore)

### 1. 파일 비교 (`diff`)

[cite_start]`git diff` 명령을 사용하여 Git의 영역 간 파일 변경 내용을 비교합니다[cite: 10, 12].

| 비교 대상 | 명령 | 설명 |
| :--- | :--- | :--- |
| **작업 D. vs 스테이징 A.** | `\$ git diff` | [cite_start]수정한 후 **아직 `add` 하지 않은** 변경 내용 확인[cite: 10, 12]. |
| **스테이징 A. vs 깃 저장소** | `\$ git diff --staged` (또는 `--cached`) | [cite_start]`add`는 했지만 **아직 `commit` 하지 않은** 변경 내용 확인[cite: 10, 12]. |
| **작업 D. vs 깃 저장소** | `\$ git diff HEAD` | [cite_start]작업 디렉토리의 파일과 **최신 커밋** 간의 모든 차이를 확인합니다[cite: 10]. |
| **두 커밋 간 비교** | `\$ git diff [CID1] [CID2]` | [cite_start]특정 커밋 이력 간의 차이를 확인합니다[cite: 10]. |

### 2. 파일 삭제 (`rm`)

파일을 Git의 관리 대상에서 삭제하거나, 작업 디렉토리에서 제거합니다.

| 명령 | 삭제되는 영역 | 특징 |
| :--- | :--- | :--- |
| `\$ rm [file]` | **작업 디렉토리** | 리눅스 명령. [cite_start]Git은 해당 파일을 **수정됨/삭제됨(Modified/Deleted)**으로 인식합니다[cite: 11, 12]. |
| `\$ git rm [file]` | **작업 D. & 스테이징 A.** | Git 명령. [cite_start]다음 커밋 시 **삭제가 반영**되도록 스테이징 영역에 표시됩니다[cite: 11, 12]. |
| `\$ git rm --cached [file]` | **스테이징 A.** | [cite_start]파일을 **Git 관리 대상에서 제외**하고 작업 디렉토리에는 남깁니다[cite: 11, 12]. |

### 3. 파일 복원 (`restore`)

[cite_start]`git restore`는 파일의 변경 내용을 되돌리거나, 삭제된 파일을 복원하는 데 사용됩니다[cite: 11, 12].

| 복원 명령 | 복원되는 영역 | 복원하는 내용의 출처 |
| :--- | :--- | :--- |
| `\$ git restore [file]` | **작업 디렉토리** | [cite_start]**스테이징 영역**에 있는 내용으로 작업 디렉토리의 변경 사항을 취소합니다[cite: 11, 12]. |
| `\$ git restore --staged [file]` | **스테이징 영역** | [cite_start]**깃 저장소(HEAD)**에 있는 내용으로 스테이징 영역의 변경 사항을 취소합니다[cite: 11, 12]. |
| `\$ git restore --source=HEAD --staged --worktree [file]` | **작업 D. & 스테이징 A.** | [cite_start]**깃 저장소(HEAD)**의 내용으로 두 영역을 모두 복구합니다 (최신 커밋 상태로 되돌림)[cite: 12]. |
| `\$ git restore --source=HEAD^ [file]` | **작업 D.** | [cite_start]**이전 커밋(HEAD^)**의 내용으로 작업 디렉토리를 복원합니다[cite: 12]. |
