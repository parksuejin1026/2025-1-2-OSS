# 💻 05 & 06장 요약: 깃 설정, 저장소 생성 및 VS Code, 리눅스 명령

본 문서는 **Visual Studio Code(VS Code)** 개요, **Git 설정 및 저장소 생성** 방법, 그리고 Git 실습에 필요한 **리눅스 기초 명령**을 요약합니다.

---

## 1. 🚀 Git 설정 (Git Configuration)

Git을 설치한 후, 커밋을 위해 사용자 신원 및 환경 설정을 전역(Global) 범위로 진행하는 것이 좋습니다.

### 1.1. 깃 설정 명령 구조 및 범위

* [cite_start]**명령 구조**: `\$ git config --설정범위 설정변수 설정값` [cite: 679, 964, 1168]
* **설정 범위**:
    * [cite_start]`--system`: 시스템의 모든 사용자와 모든 저장소에 적용[cite: 683, 885, 968, 1170].
    * [cite_start]`--global`: 현재 사용자(User)의 모든 저장소에 적용[cite: 684, 704, 885, 969, 1170]. [cite_start](설정 파일 위치: `C: Users\[사용자 계정]\.gitconfig` [cite: 707, 709, 887, 992, 994, 1172])
    * [cite_start]`--local`: 현재 저장소에만 적용 (기본값)[cite: 685, 885, 970, 1170].

### 1.2. 저장소 생성 전 필수 6가지 전역 설정 (`--global`)

| 명령 | 설명 |
| :--- | :--- |
| `\$ git config --global user.name "사용자 이름"` | [cite_start]커밋에 사용할 **사용자 이름** 설정[cite: 764, 875, 894, 1049, 1160, 1179]. |
| `\$ git config --global user.email 사용자 전자메일` | [cite_start]커밋에 사용할 **전자메일** 설정[cite: 764, 875, 895, 1049, 1160, 1180]. |
| `\$ git config --global core.editor 'code --wait'` | [cite_start]기본 편집기를 **VS Code**로 설정[cite: 764, 875, 901, 1049, 1160, 1186]. |
| `\$ git config --global init.defaultBranch main` | [cite_start]Git 저장소의 **기본 브랜치 이름**을 `main`으로 설정[cite: 764, 875, 903, 1049, 1160, 1188]. |
| `\$ git config --global core.autocrlf true` | [cite_start]Windows 환경에서 **줄바꿈(CRLF/LF) 자동 변환** 설정[cite: 729, 737, 764, 875, 897, 1014, 1022, 1049, 1160, 1182]. |
| `\$ git config --global core.safecrlf false` | [cite_start]줄바꿈 관련 **경고 메시지 발생을 방지**하도록 설정[cite: 744, 752, 764, 875, 899, 1029, 1037, 1049, 1160, 1184]. |

---

## 2. 📁 Git 저장소 생성 및 관리

### 2.1. Git 저장소 생성 (`git init`)

[cite_start]디렉토리를 Git 저장소로 초기화하여 버전 관리를 시작합니다[cite: 781, 1067].
* [cite_start]`\$ git init .`: **현재 디렉토리**를 저장소로 초기화[cite: 785, 910, 1070, 1195].
* [cite_start]`\$ git init basic`: 현재 폴더 하부에 `basic` 폴더를 생성하고 저장소로 초기화[cite: 787, 912, 1072, 1197].

### 2.2. 저장소 확인 및 삭제
* [cite_start]**저장소 확인**: 저장소로 설정된 폴더 안에 **`.git`** 이라는 숨겨진 폴더가 생성되었는지 확인합니다 (`ls -al` 명령 사용)[cite: 800, 804, 819, 1085, 1089, 1104].
* [cite_start]**저장소 삭제**: `.git` 폴더를 삭제하면 해당 폴더는 깃 저장소로서의 기능을 상실합니다[cite: 607, 822, 823, 1107, 1108].
    * [cite_start]`\$ rm -rf .git`: `.git` 폴더를 강제로(f) 재귀적(r)으로 삭제[cite: 514, 515, 516, 517, 608, 609, 610].

---

## 3. 🖥️ Visual Studio Code (VS Code)

### 3.1. 개요 및 특징
* [cite_start]MS사가 개발한 **오픈 소스 코드 편집기** (vscode)[cite: 33, 34].
* [cite_start]가볍지만 강력하며, Windows, macOS, Linux에서 사용 가능[cite: 35, 37].
* [cite_start]**확장 기능(extensions)** 에코 시스템을 활용하여 다양한 언어 및 런타임을 지원[cite: 39, 40, 41].
* [cite_start]**시스템 버전(System Installer)**으로 설치하면 모든 사용자가 이용 가능하며, `C: Program Files\Microsoft VS Code`에 설치됩니다[cite: 96, 97, 98, 99].

### 3.2. 설치 시 유용한 추가 작업 (Windows)
[cite_start]탐색기에서 바로 **'Code(으)로 열기'** 메뉴를 사용할 수 있도록 다음 항목을 선택하는 것이 편리합니다[cite: 209, 210, 233, 234, 619]:
* [cite_start]"Code(으)로 열기" 작업을 Windows 탐색기 파일의 상황에 맞는 메뉴에 추가[cite: 220, 247, 302].
* [cite_start]"Code(으)로 열기" 작업을 Windows 탐색기 디렉터리의 상황에 맞는 메뉴에 추가[cite: 221, 248, 303].
* [cite_start]PATH에 추가(다시 시작한 후 사용 가능)[cite: 223, 250, 306].

---

## 4. 🐧 리눅스 기초 명령 (Git CLI 환경)

Git 실습 시 파일 및 폴더 관리에 필요한 기본 명령입니다.

### 4.1. 폴더 및 파일 관리

| 명령 | 설명 |
| :--- | :--- |
| `\$ pwd` | [cite_start]현재 작업 디렉토리 경로 출력 (**P**rint **W**orking **D**irectory)[cite: 452, 453, 454, 623]. |
| `\$ ls` | [cite_start]파일 및 폴더 목록 출력 (**L**i**s**t)[cite: 459, 460]. |
| `\$ touch fname` | [cite_start]빈 파일 `fname` 생성[cite: 478, 479, 625]. |
| `\$ cat fname` | [cite_start]파일의 내용(텍스트)을 화면에 출력 (**Cat**enate)[cite: 495, 496, 552, 627]. |
| `\$ echo string` | [cite_start]문자열을 터미널에 출력[cite: 480, 483, 626]. |
| `\$ cp a b` | [cite_start]파일 `a`를 `b`로 복사[cite: 497, 498]. |
| `\$ mv f1 f2` | [cite_start]파일 `f1`의 이름을 `f2`로 수정하거나 이동[cite: 499, 500]. |
| `\$ rm fname` | [cite_start]파일 `fname` 삭제 (**R**e**m**ove)[cite: 512, 513]. |
| `\$ ls -l` | [cite_start]파일의 상세 정보 (권한, 소유자, 크기 등) 표시[cite: 462, 529, 530, 624]. |

### 4.2. 리다이렉트와 파이프

| 명령 | 기호 | 설명 |
| :--- | :--- | :--- |
| **리다이렉트** | `>` | [cite_start]화면의 출력 결과를 파일로 저장하며, **기존 내용을 덮어씁니다**[cite: 572, 573, 574, 587, 588]. |
| **리다이렉트** | `>>` | [cite_start]화면의 출력 결과를 파일로 저장하며, **기존 내용 뒤에 덧붙여서** 저장합니다[cite: 572, 575, 576, 589, 590]. |
| **리다이렉트** | `<` | [cite_start]**파일의 데이터**를 명령의 입력으로 사용합니다[cite: 577, 578]. |
| **파이프** | `|` | [cite_start]앞 명령의 **표준 출력**을 뒤 명령의 **표준 입력**으로 연결합니다[cite: 557, 558]. |
