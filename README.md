# alx-higher_level_programming

# git alias 
```sh
git config --global alias.acp '!f() { MESSAGE=${1:-"$(date +\%Y\-\%m\-\%d\ \%I:\%M:\%S\ \%p)"}; git add . && git commit -m "$MESSAGE" && git push; }; f'
```