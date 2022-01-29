# git 커맨드

- git add . (파일 추가)
- git commit -m "message" (커밋 작성)
- git push origin master (원격 푸쉬)

- git branch test (생성만)
- git checkout -b test (생성 후 전환)

- git branch -d test (로컬 브랜치 삭제)
- git push origin -d test (원격 브랜치 삭제)

- git checkout master (브랜치 전환)

- git merge master (브랜치 병합)
- git merge master --no-ff (브랜치 병합 커밋 남기기)

- git remote -v
- git remote add origin https://github.com/user/repo.git

### 최근 커밋 삭제 (HEAD 끝에 "~n"를 붙이면 최근 n개의 커밋 내역을 삭제한다.)
- git reset HEAD^
- git push -f origin [브랜치 명]
