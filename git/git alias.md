# Git Alias

- git alias
  - 원하는 명령어를 다른 이름으로 정해서 쓸 수 있다.
  - 자주 쓰는 명령어 혹은 긴 명령어를 정해두고 쓰면 편하다.



- 설정 방법
  - `git config alias.(사용할 이름) "사용할 명령어"`
    - ex. `git config alias.s "status -s"` : git status -s 라는 명령어를 git s 로 바꾸어 쓸 수 있다.
  - `git config --global alias.(사용할 이름) "사용할 명령어"` 로 글로벌 설정을 할 수 있다.
  - git bash에서 `vim ~/.gitconfig` 명령어를 통해 vim 편집기로 [alias] 부분에 직접 설정할 수 있다. 



- 자주 쓰는 git alias

  ```git
  git config --global alias.s "status -s"
  git config --global alias.co "checkout"
  git config --global alias.ci "commit"
  git config --global alias.br "branch"
  ```



- 유용한 alias

  ```git
  git config --global alias.l "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr)%C(bold blue)<%an>%Creset' --abbrev-commit"
  ```

  - 커밋 로그가 그래프로 나타나며, 커밋 해시는 빨간색, 브랜치 정보는 노란색, 날짜는 초록색, 작성자는 파란 색으로 구분되어 나타난다.



[출처 : 기계인간 블로그](https://johngrib.github.io/wiki/git-alias/)