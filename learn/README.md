# alx-higher_level_programming

# Git Aliases

## Add, Commit, and Push (acp)
```sh
git config --global alias.acp '!f() { MESSAGE=${1:-"$(date +\%Y\-\%m\-\%d\ \%I:\%M:\%S\ \%p)"}; git add . && git commit -m "$MESSAGE" && git push; }; f'
```

## Pull, Add, Commit, and Push (pacp)
```sh
git config --global alias.pacp '!f() { MESSAGE=${1:-"$(date +\%Y\-\%m\-\%d\ \%I:\%M:\%S\ \%p)"}; git pull && git add . && git commit -m "$MESSAGE" && git push; }; f'
```

## Status and Log (slog)
```sh
git config --global alias.slog 'log --oneline --graph --all --decorate'
```

## #!/usr/bin/python3