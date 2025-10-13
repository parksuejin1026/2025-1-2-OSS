📖 Git 학습 자료 정리
📌 3장. 커밋과 로그 이력, 과거 여행 (Commit, Log History, Time Travel)
1. 깃의 3가지 영역 (Three Areas of Git)
Git이 파일을 관리하는 주요 3가지 영역입니다.


영역 이름	영문 명칭	설명
작업 디렉토리	Working Directory (Working Tree)	
실제 파일 수정 작업이 이루어지는 사용자 폴더 

스테이징 영역	Staging Area (Index)		
git add 명령어로 다음 커밋에 포함할 파일의 스냅샷을 준비하는 임시 공간 

깃 저장소	Git Repository (Git Local Repository)	
커밋된 버전들이 저장되는 곳(.git 폴더 내) 


2. 기본 설정 및 저장소 생성
명령어	설명
\$ git config --global user.name hskang	
사용자 이름 설정 


\$ git config --global user.email hskang@gmail.com		
전자메일 설정 


\$ git config --global core.editor 'code --wait'	
기본 편집기 설정 


\$ git config --global init.defaultBranch main	
기본 브랜치 이름을 main으로 설정 


\$ git init basic	
현재 위치에 basic 저장소 생성 (초기화) 





\$ cd basic	
생성된 basic 폴더로 이동 


\$ ls -al	
파일 확인 (.git 폴더 확인) 


3. 파일 생성 및 버전 관리 (Commit)
명령어	설명	비고
\$ echo aaa > hello.txt		
hello.txt 파일 생성 및 내용 (aaa) 입력 

>: 덮어쓰기, >>: 추가 

\$ git status (-s, --short)	
깃 저장소의 현재 상태를 확인 


?? hello.txt: 추적되지 않는 파일 (untracked file) 

\$ git add hello.txt	
파일을 작업 디렉토리 → 스테이징 영역으로 이동(복사) 


\$ git commit -m 'A'		
스테이징 영역 → 깃 저장소로 스냅샷을 저장 (버전 관리) 





-m: 커밋 메시지 직접 입력 

\$ git commit -am 'B'	
수정된(Modified) 파일에 한하여 add와 commit을 한 번에 실행 

**untracked file**은 적용 불가 


4. 버전 로그 및 커밋 정보 확인
명령어	설명	비고
\$ git log		
모든 로그 이력 정보를 자세히 표시 (기본적으로 최신 커밋부터) 




\$ git log --oneline	
로그 이력을 한 줄로 간략히 표시 (커밋 ID 7자리, HEAD/브랜치 이름, 커밋 메시지 제목) 




\$ git log --graph	
문자 그림으로 로그 이력 그래프 그리기 


\$ git log --all		
모든 브랜치의 로그 이력 표시 

\$ git log -n	
최근 n개의 로그 이력만 표시 (-2는 최근 2개) 



\$ git log --reverse		
오래된 커밋부터 표시 

--graph와 함께 사용 불가 

\$ git log [--patch | -p]	
로그 이력과 함께 파일의 변화 (이전 커밋과의 차이)를 표시 


\$ git show		
가장 마지막 커밋(HEAD)의 정보와 파일 차이(diff) 표시 



인자 없으면 HEAD 생략 

\$ git show --oneline	
커밋 로그 한 줄과 파일 차이를 표시 

\$ git show -s	
커밋 로그는 표시하지만 파일 차이는 표시하지 않음 

\$ git show [commitID | HEAD~]		
지정한 커밋의 정보와 파일 차이 표시 

5. 과거 버전으로의 이동 (Time Travel)
Git은 HEAD~, HEAD^, HEAD~2 등의 포인터로 이전 커밋을 참조할 수 있습니다.





명령어	설명	비고
\$ git checkout HEAD~		
바로 이전 커밋으로 이동 





이동 시 detached HEAD 상태가 됨 

\$ git checkout [이전 커밋]		
특정 커밋으로 이동 (HEAD~2, commitID 등) 

이동 전, 작업 상태가 깨끗(clean)해야 함 


\$ git checkout main	
브랜치의 마지막 커밋(main 브랜치의 최신 버전)으로 이동 





detached HEAD 상태에서 다시 브랜치로 돌아옴 

\$ git checkout -		
이전 checkout 위치로 이동 





git checkout 대신 사용할 수 있는 명령 



설명	git checkout	git switch
이전 커밋으로 이동		
\$ git checkout [이전커밋] 



\$ git switch -d [이전커밋] 



다른 브랜치로 이동		
\$ git checkout [branch] 



\$ git switch [branch] 



새 브랜치를 생성하고 이동		
\$ git checkout -b [newBranch] 


\$ git switch -c [newBranch] 
