# 1. 깃 설정과 저장소 생성

## 📌 깃 설정 (Git Configuration)

깃 설치 후 깃 배시(Git Bash)에서 처음 해야 할 일은 **사용자 이름**과 **전자메일**을 설정하는 것입니다.

### 1.1. 주요 설정 변수와 값

| 설정 변수 | 설정값 (예시) | 설명 |
| :--- | :--- | :--- |
| **`user.name`** | `ai7dnn` | 사용자 이름 |
| **`user.email`** | `ai7dnn@gmail.com` | 사용자 전자메일 |
| **`init.defaultBranch`** | `main` | 기본 브랜치 이름 |
| `core.editor` | `'code --wait'` 또는 `'notepad'` | 기본 편집기 설정 |
| `core.autocrlf` | `true` (윈도) \| `input` (맥/리눅스) | 줄바꿈 자동 변환 |
| `core.safecrlf` | `true` 또는 `false` | 줄바꿈 안전 확인 |

### 1.2. 설정 명령 구조 및 범위

* **명령 구조:** `$ git config --설정범위 설정변수 설정값`
* **설정 범위:**
    * `--system`: **모든 사용자**에게 적용.
    * **`--global`**: **현재 사용자**의 **모든 저장소**에 적용 (가장 많이 사용).
    * `--local`: 현재 사용자의 **현재 저장소**에만 적용.

### 1.3. 전역 설정 파일

* `--global` 옵션으로 설정한 내용은 **`.gitconfig`** 파일에 저장됩니다.
* **윈도**의 경우, 저장 위치는 일반적으로 `C:\Users\[사용자 계정]\.gitconfig`입니다.
* **전역 설정 파일 편집 명령:** `$ git config --global --edit` 또는 `$ git config --global -e`.

### 1.4. 저장소 생성 전 필수 6가지 설정 명령 (Global)

| 설정 내용 | 주요 명령 (예시) |
| :--- | :--- |
| **사용자 이름** | `$ git config --global user.name "ai7dnn"` |
| **사용자 전자메일** | `$ git config --global user.email ai7dnn@gmail.com` |
| **줄바꿈 자동 변환** | `$ git config --global core.autocrlf true` (윈도 권장) |
| **줄바꿈 안전 설정** | `$ git config --global core.safecrlf false` (경고 방지) |
| **기본 편집기 설정** | `$ git config --global core.editor 'code --wait'` |
| **기본 브랜치 이름** | `$ git config --global init.defaultBranch main` |

> 💡 **줄바꿈 설정 이유:** 플랫폼마다 줄 끝을 인식하는 방법이 다릅니다. (Windows: CR+LF, Mac/Linux: LF).

## 📌 깃 저장소 생성 (Git Repository Creation)

디렉토리를 **Git Repository**로 만들어야 깃으로 버전 관리가 가능합니다.

### 2.1. 저장소 생성 명령 (`git init`)

| 명령 | 설명 |
| :--- | :--- |
| **`$ git init`** 또는 **`$ git init .`** | **현재 디렉토리**를 깃 저장소로 생성. |
| **`$ git init [폴더이름]`** (예: `$ git init basic`) | 현재 폴더 하부에 새로운 **폴더**(`basic`)를 **생성**하고 깃 저장소로 만듭니다. |

### 2.2. 저장소 확인 및 삭제

* 저장소 생성 확인: 생성된 폴더 내부에 **`.git`** 폴더가 있는지 확인합니다.
* `.git` 폴더: **커밋된 모든 파일의 모든 버전 기록**이 저장됩니다.
* `.git` 폴더를 삭제하면 **깃 저장소로서의 기능을 상실**합니다.
* **저장소 삭제 명령:** `$ rm -rf .git` (저장소 기능 상실 후 다시 설정 가능).

---

# 2. Visual Studio Code와 리눅스 명령

## 💻 1. Visual Studio Code (VS Code) 개요 및 설치

### 1.1. VS Code 개요

* Microsoft사가 개발한 **오픈소스 에디터 소프트웨어** (코드 에디터).
* 가볍지만 강력하며, Windows, macOS, Linux 등 **모든 운영체제**에서 사용 가능.
* **기본 지원 언어:** JavaScript, TypeScript, Node.js.
* **확장 기능(Extension) 에코 시스템**을 통해 C++, Python, Java 등 다양한 언어 지원.
* 파일 편집과 **버전 관리(Git)**도 지원.

### 1.2. 설치 권장 사항 및 옵션

* **시스템 버전 (System Installer) 설치 권장**.
    * 시스템 기본 폴더에 설치되어 해당 컴퓨터의 모든 사용자가 사용 가능합니다.
* **추가 작업 선택 시 권장 옵션 (편의성 증대)**:
    * **"Code(으)로 열기"** 작업을 Windows 탐색기 **파일**의 상황에 맞는 메뉴에 추가.
    * **"Code(으)로 열기"** 작업을 Windows 탐색기 **디렉터리**의 상황에 맞는 메뉴에 추가.

### 1.3. VS Code 실행 화면 주요 구성 요소

* **활동바 (Activity Bar):** 탐색기, 검색, 소스 제어, 실행 및 디버그, 확장 등의 개별 아이콘 제공.
* **사이드바 (Sidebar)**.
* **메뉴 (Menu)**.
* **편집기 (Editor)**.
* **상태바 (Status Bar)**.

## ⚙️ 2. 리눅스 기초 명령 (Git 실습용)

| 명령 유형 | 명령 (예시) | 설명 |
| :--- | :--- | :--- |
| **현재 위치** | `$ pwd` | Print Working Directory: **현재 폴더 표시**. |
| **폴더 이동** | `$ cd [폴더이름]` | Change Directory: 폴더 이동. |
| **폴더 생성** | `$ mkdir [dname]` | Make Directory: 폴더 생성. |
| **파일/폴더 목록** | `$ ls` | File or folder list: 목록 조회. |
| | `$ ls -al` | **상세 정보(`-l`)**와 **숨김 파일(`-a`)** 포함하여 목록 표시. |
| **파일 생성** | `$ touch [fname]` (예: `a.txt`) | 빈 파일 생성. |
| **내용 출력** | `$ echo [문자열]` (예: `aaa`) | 문자열을 컴퓨터 터미널에 출력. |
| **파일 내용 보기** | `$ cat [fname]` (예: `a.txt`) | 파일의 내용을 화면에 출력. |
| **파일 복사** | `$ cp [a] [b]` | 파일 `a`를 `b`로 복사. |
| **이름 변경** | `$ mv [f1] [f2]` | 파일 `f1`을 `f2`로 이름 수정 (이동도 가능). |
| **파일 삭제** | `$ rm [fname]` | 파일 삭제. |
| **폴더 삭제** | `$ rm -rf [dname]` | 하부에 서브 폴더/파일이 있어도 폴더를 **강제로(`-f`) 재귀적(`-r`)**으로 삭제. |

### 2.1. 리다이렉션 (Redirection)

| 기호 | 설명 | 활용 사례 |
| :--- | :--- | :--- |
| **`>`** | 화면의 출력 결과를 파일로 저장 (**기존 내용을 지우고** 저장/대체). | `$ echo aaa > a.txt` (a.txt에 "aaa" 저장). |
| **`>>`** | 화면의 출력 결과를 파일로 저장 (**기존 내용 뒤에 덧붙여서** 저장/추가). | `$ echo bbb >> a.txt` (a.txt에 "bbb" 추가). |
| **`<`** | 파일의 데이터를 명령에 **입력**. | `$ cat < file1` (file1의 내용을 출력). |

### 2.2. 파이프 (Pipe)

* **기호:** `|` (vertical bar)
* **설명:** 앞 명령의 **표준 출력**을 뒤 명령의 **표준 입력**으로 처리.
* **활용 예:** `$ cat file1 file2 | more` (파일 내용을 페이지별로 출력).
