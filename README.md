# Sample_to_learn_security_functions
A small learning repository demonstrating GitHub security features.

What this repo includes:

- Basic Python sample app (`app.py`) and `requirements.txt`.
- `SECURITY.md` and `CODEOWNERS` to show responsible disclosure and ownership.
- `dependabot.yml` to demonstrate automated dependency updates.
- GitHub Actions workflows for automated security checks (`bandit`, `safety`) and secret scanning (`trufflehog`).

Quick local checks

1. Create a virtualenv and install deps:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install bandit safety
```

2. Run the security tools locally:

```bash
bandit -r .
safety check
```

See the `.github` folder for CI workflow examples and `SECURITY.md` for disclosure.
