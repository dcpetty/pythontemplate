# pythontemplate

This is a template for a Python project.

## Steps to follow

These steps are based on Github account `dcpetty` with private e-mail address `dcpetty@users.noreply.github.com` and with this repository `pythontemplate` being copied into repository `newpython`. Change these to match your account and repository.

- Follow the [Duplicating a repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/duplicating-a-repository) documentation to duplicate this repository `pythontemplate` to repository `newpython`.
- Enable *GitHub Pages* for the `main` branch from *Settings*.
- `git clone` the repository into the parent directory of the `newpython` local branch.
  - Use `git clone git@github.com:dcpetty/pythontemplate.git` from the SSH tab of the `<> Code` button directly. *Or&hellip;* 
  - Use `git clone https://github.com/dcpetty/newpython.git` from the HTTPS tab of the `<> Code` button and:
    - Change the `.git/config` `url` of the `newpython` local branch as per [`https://gist.github.com/jexchan/2351996`](https://gist.github.com/jexchan/2351996) as follows:
      - from: `url = https://github.com/dcpetty/newpython.git`
      - to: `url = git@github.com:dcpetty/newpython.git`
- This SSH configuration is based on having followed the *[Generating a new SSH key and adding it to the ssh-agent](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)* documentation. This presupposes that `~/.ssh/` contains the files (for example) `id_rsa_dcp` and `id_rsa_dcp.pub` and that `~/.ssh/config` then contains the following:

```
Host *
  AddKeysToAgent yes
  UseKeychain yes

Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_rsa_dcp
```

- **Note**: for these configuration to work, the key will be added to the `ssh-agent`. Use `ssh-add -l` to see which keys have been added. When generating an SSH key, I do not use a passphrase. 
 - If you *do* use a passphrase on Mac OS, use `ssh-add -K ~/.ssh/id_rsa_dcp` (for example) to add it to the Apple keychain one time. You can add `ssh-add -A 2>/dev/null` to your Z-Shell resource file `~/.zshrc` on Mac OS to initialize `ssh-agent` in each Z-Shell without needing the passphrase.
- Add the following to `.git/config` to associate commits with the correct account name:

```
[user]
  name = dcpetty
  email = dcpetty@users.noreply.github.com
```

- Rename, edit, and delete the Python files (through `git`)  in `./src/`.

## Personal access tokens

It is also possible to manage the `.git/config` `url` of the `newpython` local branch with a [*personal access token*](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) (PAT) *in lieu* of using SSH. [This](https://docs.google.com/document/d/1V2_qMe-OUUC51dH1J2bZy4UoIG78nC3zzaaMcAimeYs/) document describes the Github command-line interface in detail.

For this example, with a PAT of <code>&#x67;&#x68;&#x70;&lowbar;&#x61;&#x4d;&#x47;&#x43;&#x75;&#x59;&#x4c;&#x4f;&#x59;&#x6d;&#x56;&#x76;&#x54;&#x33;&#x41;&#x54;&#x64;&#x78;&#x6a;&#x6e;&#x70;&#x30;&#x6e;&#x35;&#x36;&#x65;&#x53;&#x74;&#x31;&#x6d;&#x32;&#x69;&#x6b;&#x49;&#x59;&#x75;</code>, the `.git/config` HTTPS `url` of the `newpython` local branch should be changed as follows:

- from: `url = https://github.com/dcpetty/newpython.git`
- to: <code>&#x75;&#x72;&#x6c;&#x20;&equals;&#x20;&#x68;&#x74;&#x74;&#x70;&#x73;&colon;&sol;&sol;&#x64;&#x63;&#x70;&#x65;&#x74;&#x74;&#x79;&colon;&#x67;&#x68;&#x70;&lowbar;&#x61;&#x4d;&#x47;&#x43;&#x75;&#x59;&#x4c;&#x4f;&#x59;&#x6d;&#x56;&#x76;&#x54;&#x33;&#x41;&#x54;&#x64;&#x78;&#x6a;&#x6e;&#x70;&#x30;&#x6e;&#x35;&#x36;&#x65;&#x53;&#x74;&#x31;&#x6d;&#x32;&#x69;&#x6b;&#x49;&#x59;&#x75;&commat;&#x67;&#x69;&#x74;&#x68;&#x75;&#x62;&period;&#x63;&#x6f;&#x6d;&sol;&#x64;&#x63;&#x70;&#x65;&#x74;&#x74;&#x79;&sol;&#x6e;&#x65;&#x77;&#x70;&#x79;&#x74;&#x68;&#x6f;&#x6e;&period;&#x67;&#x69;&#x74;</code>

Notes about PATs:

- PATs are created under Account Settings > Developer Settings > Personal Access Tokens > Tokens (classic). Once created, you must copy a PAT before closing that page, because they cannot be accessed after that point except to be deleted.
- PATs are set with an expiration date when created. As long as they have not expired (or been deleted), the `url` that includes a PAT can be used *to access any repo with you as the user* without logging in. **Keep them secure and do not give general access to `.git/config` files that include them.**
- You cannot include a PAT in any documents pushed to the repo, or the PAT will be deleted by Github.

## Command-line argument parsing using [`argparse`](https://docs.python.org/3/library/argparse.html)

[`template.py`](https://github.com/dcpetty/pythontemplate/blob/main/src/template.py) parses example command-line arguments with [`argparse`](https://docs.python.org/3/library/argparse.html). `argparse` allows for command-line argument types of *required*, *optional*, *flagged*, and *flagged multiple*. Any *required* and *optional* command-line arguments must be grouped together either before or after *flagged*, and *flagged multiple* command-line arguments which themselves must be grouped together.

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

## Updated `.gitignore`

The following basic `.gitignore` prefix is a useful starting point (and includes `.git/info/exclude`). Add files generated by [https://gitignore.io/](https://gitignore.io/) to that prefix &mdash; in [this](https://github.com/psb-david-petty/pythontemplate/blob/main/.gitignore) case those for `c,c++,jekyll,java,python,r,git,latex,macos,intellij+all,pycharm+all,visualstudiocode`.

```git
######################################################################
# git ls-files --others --exclude-from=.git/info/exclude
# Lines that start with '#' are comments.
# For a project mostly in C, the following would be a good set of
# exclude patterns (uncomment them if you want to use them):
*.[oa]
*~

# IDE files #
#############
*.bluej
*.drjava
*.gpj
*.eml
*.userlibraries
.project
.classpath

# IDE directories #
###################
.settings/
bin/

# User directories #
####################
.git/
.m2/
.gradle/

# Target build directories #
############################
target/
build/
out/

# Compiled source #
###################
*.com

# Packages #
############
*.7z
*.dmg
*.gz
*.iso
*.bz2

# Databases #
#############
*.sql
*.sqlite
```

<hr>

[&#128279; permalink](https://dcpetty.github.io/pythontemplate) and [&#128297; repository](https://github.com/dcpetty/pythontemplate) for this page.
