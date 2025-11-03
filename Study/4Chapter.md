# Git 챕터 4: 파일 비교 (Diff), 삭제 (Rm), 복원 (Restore) 정리

## 1. 파일 비교 명령: git diff (차이점 확인)

`git diff` 명령은 깃의 3가지 영역(Working Directory, Staging Area, Git Repository) 간의 **차이점**을 비교하여 보여줍니다.

### 1.1. 깃 3 영역 간 파일 비교

| 명령 | 비교 대상 (기준 ← 대상) | 주요 확인 내용 |
| :--- | :--- | :--- |
| **`$ git diff`** | Staging Area ← Working Directory | `add`를 아직 하지 않은, **작업 디렉토리의 수정 내용** |
| **`$ git diff --staged`** | HEAD (Repository) ← Staging Area | `add`는 했지만 `commit`은 아직 안 한, **다음 커밋에 포함될 내용** |
| **`$ git diff HEAD`** | HEAD (Repository) ← Working Directory | **최신 커밋 이후 발생한 모든 수정 내용** (`add` 여부 무관) |

### 1.2. 커밋 간 파일 비교

특정 두 커밋 또는 브랜치 간의 파일 상태 차이를 비교합니다.

| 명령 | 비교 대상 | 설명 |
| :--- | :--- | :--- |
| **`$ git diff [commitID1] [commitID2]`** | 두 커밋 | 특정 두 커밋 상태 간의 차이를 비교 |
| **`$ git diff HEAD~ HEAD`** | 바로 이전 커밋과 현재 커밋 | 최신 커밋에서 발생한 변경 사항 |

> 💡 **심화 팁: Diff를 읽는 법**
> `git diff` 결과에서 파일명 앞의 `a/`는 **기준 파일(비교 전)**, `b/`는 **대상 파일(비교 후)**을 의미하며, `+`는 추가된 줄, `-`는 삭제된 줄을 나타냅니다.

---

## 2. 파일 삭제 및 추적 중지 명령: git rm

| 명령 | 역할 및 설명 |
| :--- | :--- |
| **`$ rm [file]`** | **(주의: 리눅스 명령)** Working Directory에서만 파일을 삭제합니다. Git은 이 파일을 '삭제됨(deleted)'으로 인지하여 Staging Area에 반영해야 합니다. |
| **`$ git rm [file]`** | Working Directory와 Staging Area에서 모두 파일을 삭제하고, 다음 커밋 시 이 삭제를 기록하도록 **자동으로 준비**합니다. (가장 일반적인 Git 삭제 방법) |
| **`$ git rm --cached [file]`** | **Staging Area에서만 추적을 해제**합니다. Working Directory의 파일은 그대로 유지됩니다. (실수로 추적했거나, 이미 커밋된 파일을 `.gitignore`로 관리하고 싶을 때 유용) |

---

## 3. 파일 복원 명령: git restore (되돌리기)

`git restore`는 파일의 변경 내용을 되돌리는 데 사용되는 가장 명확하고 최신 명령입니다.

### 3.1. Working Directory의 변경 내용 복원 (수정 취소)

| 명령 | 복원 기준 | 복원 대상 | 주요 사용 목적 |
| :--- | :--- | :--- | :--- |
| **`$ git restore [file]`** | Staging Area의 내용 | Working Directory | Working Directory에서 수정한 내용을 취소하고, **최근 `git add` 상태**로 되돌립니다. |
| **`$ git restore --source=HEAD [file]`** | HEAD (Repository)의 내용 | Working Directory | Working Directory에서 수정한 내용을 취소하고, **최신 커밋 상태**로 되돌립니다. |

### 3.2. Staging Area의 내용 복원 (Unstaging)

| 명령 | 복원 기준 | 복원 대상 | 주요 사용 목적 |
| :--- | :--- | :--- | :--- |
| **`$ git restore --staged [file]`** | HEAD (Repository)의 내용 | Staging Area | Staging Area에서 `add`한 상태를 취소하고, **최신 커밋 상태**로 되돌립니다. (`git reset HEAD [file]`의 대안) |

### 3.3. 완전 복원

| 명령 | 복원 기준 | 복원 대상 | 설명 |
| :--- | :--- | :--- | :--- |
| **`$ git restore --source=HEAD --staged --worktree [file]`** | HEAD | Staging + Working | 최신 커밋 상태로 Staging Area와 Working Directory **모두**를 한 번에 되돌립니다. |

---

## 👨‍💻 좋은 개발자가 되기 위한 Git 활용 심화 팁

### 1. 'Reset' vs 'Restore' 명확히 구분하기

| 명령 | 용도 | 목표 |
| :--- | :--- | :--- |
| **`git restore`** | **파일 내용** 복원 | Working Directory나 Staging Area의 **파일 내용**을 되돌립니다. (커밋 이력에 영향 없음) |
| **`git reset`** | **커밋 포인터** 이동 | HEAD(현재 위치)를 **특정 커밋으로 이동**시키고, 필요에 따라 Staging Area나 Working Directory 상태를 변경합니다. (주로 커밋 이력을 되돌릴 때 사용) |

**🔥 핵심:** Git에서 '시간 여행'은 `git checkout/switch`나 `git reset`을 사용하지만, **단순히 파일의 수정 사항만 되돌릴 때**는 **`git restore`**를 사용해야 안전하고 의도가 명확합니다.

### 2. `git diff`는 충돌 해결의 기본

협업 환경에서 코드를 병합(Merge)하거나 리베이스(Rebase)할 때 **충돌(Conflict)**이 자주 발생합니다. 충돌을 해결하는 과정은 결국 '두 브랜치/커밋 간의 차이'를 파악하는 **`git diff`**의 원리를 이해하는 것에서 시작합니다. Diff를 통해 어떤 줄이 추가/삭제/수정되었는지 정확히 읽는 습관을 들이세요.

### 3. `.gitignore` 파일의 중요성

`git rm --cached`는 종종 **실수로 커밋한 파일을 추적 대상에서 제외**하고 싶을 때 사용됩니다. 이 명령으로 추적을 해제한 후, 해당 파일을 반드시 `.gitignore` 파일에 추가하여 Git이 해당 파일을 영원히 무시하도록 설정해야 합니다.