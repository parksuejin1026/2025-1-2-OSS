# Git 챕터 3: 커밋과 로그 이력 정리

## 1. 깃의 3가지 영역과 커밋 과정

Git은 세 가지 영역(**Working Directory, Staging Area, Git Repository**)을 통해 버전을 관리합니다.

### 1.1. 깃 3 영역 개요

| 영역 | 별칭 | 역할 및 위치 |
| :--- | :--- | :--- |
| **작업 디렉토리 (Working Directory)** | Working Tree | 실제 파일을 생성하고 수정하는 공간 (탐색기 상의 폴더). |
| **스테이징 영역 (Staging Area)** | Index | 커밋할 파일을 준비하는 공간 (저장소의 `.git` 폴더 내 파일). |
| **깃 저장소 (Git Repository)** | - | 버전 관리를 위해 **스냅샷(Snap Shot)**이 저장되는 곳. |

### 1.2. 파일 상태 변화 및 커밋 명령

버전 관리를 위해 파일을 **Working Tree**에서 **Staging Area**로 `add`하고, **Staging Area**에서 **Git Repository**로 `commit`해야 합니다.

| 명령 | 역할 및 설명 |
| :--- | :--- |
| **`$ git add [file]`** | 파일을 Working Directory에서 Staging Area로 복사합니다. |
| **`$ git commit -m 'message'`** | 현재 Staging Area의 내용에 대해 스냅샷을 찍어 깃 저장소에 저장하며, 커밋 메시지를 직접 입력합니다. |
| **`$ git commit -am 'message'`** | 이미 추적 중인 **수정된 파일**에 한해 `add`와 `commit`을 한 번에 실행합니다. (**Untracked file은 불가**). |
| **`$ git commit`** | 옵션 `-m`을 사용하지 않으면, 기본 편집기(예: VS Code)가 실행되어 커밋 메시지를 입력하고 저장해야 합니다. |
| **`$ git rm --cached [file]`** | Staging Area에서 파일을 제거합니다 (**Unstaging**). |

### 1.3. 깃 상태 확인 (`git status`)

| 명령 | 설명 |
| :--- | :--- |
| **`$ git status`** / **`--long`** | 깃 저장소의 현재 상태를 자세히 확인합니다. |
| **`$ git status -s`** / **`--short`** | 현재 상태를 간단히 표시합니다. |

> 💡 **주요 파일 상태 표시 (Short Status `-s`):**
> * **`?? [file]`**: **Untracked file** (추적되지 않는 파일).
> * **`A [file]`**: **A**dded (Staging Area에 추가됨).
> * **`M [file]`**: **M**odified (작업 디렉토리에서 수정됨).
> * **`nothing to commit, working tree clean`**: 3 영역이 동일한 상태입니다.

---

## 2. 버전 로그 이력과 과거 여행

### 2.1. 커밋 로그 확인 명령

| 명령 | 옵션 | 설명 |
| :--- | :--- | :--- |
| **`$ git log`** | (기본) | 로그 이력 정보를 표시하며, 기본적으로 **가장 최근 커밋부터** 표시합니다. |
| | **`--oneline`** | 로그 이력을 **한 줄로 간략히** 표시합니다. (커밋 ID 7자리, HEAD, 브랜치 이름, 메시지 제목). |
| | **`--patch`** / **`-p`** | 로그 이력과 함께 **파일의 변화(이전 커밋과의 차이)**를 표시합니다. |
| | **`--graph`** | 문자 그림으로 로그 이력을 그립니다. |
| | **`--all`** | 모든 브랜치의 로그 이력을 표시합니다. |
| | **`--reverse`** | **오래된 커밋부터** 표시합니다. |
| | **`-n`** | 최근 `n`개의 로그 이력을 표시합니다. |

### 2.2. 커밋 상세 정보 확인 (`git show`)

| 명령 | 옵션 | 설명 |
| :--- | :--- | :--- |
| **`$ git show`** | (기본) | **마지막 커밋(HEAD)의 정보**와 **이전 버전과의 파일 차이(diff)**를 표시합니다. |
| | **`--oneline`** | 커밋 로그 한 줄과 파일 차이를 표시합니다. |
| | **`-s`** | 파일 차이는 표시되지 않습니다. |
| **`$ git show [commitID]`** | - | 지정한 커밋 ID의 커밋 정보를 표시합니다. |

### 2.3. 과거 버전 이동 (시간 여행)

| 표현 | 의미 |
| :--- | :--- |
| **`HEAD`** | 현재 작업 중인 브랜치의 최신 커밋을 가리키는 포인터. |
| **`HEAD~`** / **`HEAD^`** | **하나 전 커밋** (바로 이전 버전). |
| **`HEAD~2`** / **`HEAD^^`** | **두 개 전 커밋**. |

| 명령 (이동 및 전환) | `git checkout` | `git switch` (권장되는 최신 명령) |
| :--- | :--- | :--- |
| **이전 커밋으로 이동** | `$ git checkout [이전커밋]` | `$ git switch -d [이전커밋]` |
| **다른 브랜치로 이동** | `$ git checkout [branch]` | `$ git switch [branch]` |
| **이전 위치로 돌아가기** | `$ git checkout -` | `$ git switch -` |
| **새 브랜치 생성 후 이동** | `$ git checkout -b [newBranch]` | `$ git switch -c [newBranch]` |

> 💡 **Detached HEAD (떨어진 HEAD) 상태:**
> * `git checkout HEAD~` 등의 명령으로 과거 커밋으로 이동했을 때 발생합니다.
> * HEAD가 브랜치 이름(main)이 아닌 특정 커밋(ID)을 가리키는 상태입니다.
> * 이 상태에서 새로운 커밋을 만들면 어떤 브랜치에도 속하지 않아 커밋이 유실될 수 있습니다.
> * **`$ git checkout main`** 또는 **`$ git switch main`** 명령으로 브랜치의 최신 커밋으로 돌아와 이 상태에서 벗어나야 합니다.

---

## 👨‍💻 좋은 개발자가 되기 위한 Git 활용 심화 팁

### 1. 좋은 커밋 메시지 작성 원칙 (Conventional Commits)

협업 시에는 **표준화된 커밋 메시지**를 사용하는 것이 필수입니다. 단순한 '수정', '추가' 대신 다음 형식을 권장합니다.
* **형식:** `<type>: <subject>`
* **예시:** `feat: 사용자 로그인 기능 추가`, `fix: 비밀번호 초기화 버그 수정`
* **주요 타입:** `feat`(기능 추가), `fix`(버그 수정), `docs`(문서 수정), `style`(스타일/포맷팅), `refactor`(리팩토링), `chore`(빌드 시스템 변경 등)
* **효과:** **코드 리뷰**가 쉬워지고, 나중에 로그(Log)를 통해 기능별 변경 이력을 자동으로 추출할 수 있게 됩니다.

### 2. 최신 커밋 수정: `git commit --amend`

작은 오타나 사소한 누락이 발생하여 **가장 최근의 커밋**을 수정해야 할 때가 있습니다. `git commit --amend`는 새로운 커밋을 만드는 대신, 이전 커밋을 덮어쓰고 **새로운 커밋 ID**를 부여합니다.
* **용도:** 방금 커밋했는데, 메시지에 오타가 났거나 파일을 빠뜨렸을 때 유용합니다.
* **명령:** `$ git add [누락된 파일]`, `$ git commit --amend`
* **주의:** 이미 **원격 저장소(GitHub 등)에 Push**한 커밋은 절대 `amend`로 수정하지 마세요. (다른 사람과의 이력이 꼬입니다. Pull Request가 없는 **로컬 작업**에서만 사용)

### 3. 로그 시각화: `git log --graph`와 Custom Format 활용

`$ git log --graph --all --oneline`는 필수입니다. 여기에 더해서, 로그를 터미널에서 더 예쁘게 시각화하려면 `format` 옵션을 활용해보세요.
* **예시:** `$ git log --all --graph --pretty=format:"%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset"`
* **효과:** 커밋 ID, 브랜치/태그 정보, 메시지, 시간, 작성자가 한눈에 들어오는 **컬러풀한 로그**를 볼 수 있어 복잡한 브랜치 이력 파악에 매우 효과적입니다.