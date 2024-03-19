# pythontemplate

This is a template for a Python project.

## Steps to follow

These steps are based on Github account `psb-david-petty` with private e-mail address `psb-david-petty@users.noreply.github.com` and with this repository `pythontemplate` being copied into repository `newpython`. Change these to match your account and repository.

- Follow the [Duplicating a repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/duplicating-a-repository) documentation to duplicate this repository `pythontemplate` to repository `newpython`.
- Enable *GitHub Pages* for the `main` branch from *Settings*.
- `git clone https://github.com/psb-david-petty/newpython.git` into the parent directory of the `newpython` local branch.
- Change the `.git/config` `url` of the `newpython` local branch as per [`https://gist.github.com/jexchan/2351996`](https://gist.github.com/jexchan/2351996) as follows:
  - from: `url = https://github.com/psb-david-petty/newpython.git`
  - to: `url = git@github.com-bhs:psb-david-petty/newpython.git`
- This SSH configuration is based on having followed the *[Generating a new SSH key and adding it to the ssh-agent](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)* documentation. The change to `git@github.com-bhs` presupposes that `~/.ssh/` contains the files `id_rsa_bhs` and `id_rsa_bhs.pub` and that `~/.ssh/config` contains the following:

```
Host *
  AddKeysToAgent yes
  UseKeychain yes

Host github.com-bhs
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_rsa_bhs
```
- **Note**: for these configuration to work, the key must be added to the `ssh-agent`. Use `ssh-add -l` to see whether the key has been added and, if not, use `ssh-add ~/.ssh/id_rsa_bhs`.
- Add the following to `.git/config` to associate commits with the correct account name:

```
[user]
  name = psb-david-petty
  email = psb-david-petty@users.noreply.github.com
```

- Rename, edit, and delete the Python files (through `git`)  in `./src/`.

## Personal access tokens

It is also possible to manage the `.git/config` `url` of the `newpython` local branch with a [*personal access token*](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) (PAT) *in lieu* of using SSH. [This](https://docs.google.com/document/d/1V2_qMe-OUUC51dH1J2bZy4UoIG78nC3zzaaMcAimeYs/) document describes the Github command-line interface in detail.

For this example, with a PAT of `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`, the `.git/config` `url` of the `newpython` local branch should be changed as follows:

- from: `url = https://github.com/psb-david-petty/newpython.git`
- to: `url = https://psb-david-petty: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@github.com/psb-david-petty/newpython.git`

Notes about PATs:

- PATs are created under Account Settings > Developer Settings > Personal Access Tokens > Tokens (classic). Once created, you must copy a PAT before closing that page, because they cannot be accessed after that point except to be deleted.
- PATs are set with an expiration date when created. As long as they have not expired (or been deleted), the `url` that includes a PAT can be used *to access any repo with you as the user* without logging in. **Keep them secure and do not give general access to `.git/config` files that include them.**
- You cannot include a PAT in any documents pushed to the repo, or the PAT will be deleted by Github.

## Command-line argument parsing using [`argparse`](https://docs.python.org/3/library/argparse.html)

[`template.py`](https://github.com/psb-david-petty/pythontemplate/blob/main/src/template.py) parses example command-line arguments with [`argparse`](https://docs.python.org/3/library/argparse.html). `argparse` allows for command-line argument types of *required*, *optional*, *flagged*, and *flagged multiple*. Any *required* and *optional* command-line arguments must be grouped together either before or after *flagged*, and *flagged multiple* command-line arguments which themselves must be grouped together.

Executing `template.py -?` from the command line shows:

```python3
usage: template.py [-?] [--version] [-a ARG] [-m MULT] [-v]
                   REQUIRED [OPTIONAL ...]

This is a template that includes argparse.ArgumentParser-style arguments in
all their various forms.

positional arguments:
  REQUIRED              required argument
  OPTIONAL              optional arguments (default: None)

optional arguments:
  -?, --help            show this help message and exit
  --version             show program's version number and exit
  -a ARG, --arg ARG     argument — multiples supersede (default: None)
  -m MULT, --mult MULT  multi-argument — multiples accumulate (default: None)
  -v, --verbose         echo status information (default: False)

```

<hr>

[&#128279; permalink](https://psb-david-petty.github.io/pythontemplate) and [&#128297; repository](https://github.com/psb-david-petty/pythontemplate) for this page.
