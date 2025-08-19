# Guia Básico de Comandos Git

Este README apresenta os principais comandos do Git, além de comandos intermediários como `git merge`, `git rebase`, `git stash` e `git cherry-pick`. Cada comando é explicado com exemplos práticos e dicas de quando utilizá-los.

---

## Comandos Básicos

### 1. `git init`

Inicializa um novo repositório Git na pasta atual.

```bash
git init
```

### 2. `git clone`

Clona um repositório remoto para sua máquina.

```bash
git clone https://github.com/usuario/repositorio.git
```

### 3. `git status`

Mostra o status dos arquivos no repositório (modificados, não rastreados, etc).

```bash
git status
```

### 4. `git add`

Adiciona arquivos ao stage para o próximo commit.

```bash
git add arquivo.txt
# Ou para adicionar todos os arquivos modificados
git add .
```

### 5. `git commit`

Salva as alterações do stage no histórico do repositório.

```bash
git commit -m "Mensagem do commit"
```

### 6. `git push`

Envia os commits locais para o repositório remoto.

```bash
git push origin main
```

### 7. `git pull`

Atualiza seu repositório local com as alterações do remoto.

```bash
git pull origin main
```

---

## Comandos Intermediários

### 1. `git merge`

Combina o histórico de duas branches. Usado para unir o trabalho de diferentes linhas de desenvolvimento.

**Quando usar:**

- Ao finalizar uma feature e querer unir à branch principal (ex: `main` ou `develop`).

**Exemplo:**

```bash
git checkout main
git merge feature-branch
```

### 2. `git rebase`

Reaplica commits de uma branch sobre outra, criando um histórico linear.

**Quando usar:**

- Para manter o histórico limpo e linear.
- Antes de um merge, para evitar muitos "commits de merge".

**Exemplo:**

```bash
git checkout feature-branch
git rebase main
```

#### Resolvendo conflitos durante o rebase

Se ocorrerem conflitos durante o rebase, o Git irá pausar e mostrar quais arquivos precisam ser resolvidos. Siga os passos:

1. Resolva os conflitos nos arquivos indicados.
2. Marque os arquivos como resolvidos:
   ```bash
   git add <arquivo-resolvido>
   ```
3. Continue o rebase:
   ```bash
   git rebase --continue
   ```
4. Repita até o rebase terminar.

**Importante:** Após um rebase, o histórico da branch é reescrito. Por isso, ao enviar para o repositório remoto, use push forçado:

```bash
git push origin <nome-da-branch> --force
```

Use o push forçado apenas em branches que não são compartilhadas com outras pessoas, para evitar sobrescrever o trabalho de outros.

### 3. `git stash`

Salva temporariamente alterações não commitadas, permitindo trocar de branch sem perder o trabalho em andamento.

**Quando usar:**

- Quando precisa mudar de branch, mas não quer commitar alterações inacabadas.

**Exemplo:**

```bash
git stash           # Salva alterações
# ...troque de branch...
git stash pop       # Recupera alterações
```

### 4. `git cherry-pick`

Aplica um commit específico de outra branch na branch atual.

**Quando usar:**

- Para aplicar uma correção ou funcionalidade específica sem trazer todos os commits de uma branch.

**Exemplo:**

```bash
git checkout main
git cherry-pick <hash-do-commit>
```

---

## Dicas Gerais

- Use `git log` para visualizar o histórico de commits.
- Sempre faça backup antes de operações como rebase ou cherry-pick.
- Consulte a documentação oficial: https://git-scm.com/doc

---

**Bons commits!**

---

## Pull Requests (PR)

Pull Request (PR) é uma solicitação para que suas alterações em uma branch sejam revisadas e, se aprovadas, integradas a outra branch (geralmente a principal, como `main` ou `develop`).

### Quando usar?

- Sempre que terminar uma feature, correção ou melhoria e quiser que outro(s) membro(s) do time revise(m) seu código antes de integrar ao projeto principal.
- Em projetos colaborativos, é a principal forma de contribuir e manter a qualidade do código.

### Como funciona?

1. Faça suas alterações em uma branch separada.
2. Suba a branch para o repositório remoto:
   ```bash
   git push origin minha-branch
   ```
3. No GitHub, GitLab ou similar, clique em "New Pull Request" e selecione sua branch de origem e a branch de destino.
4. Descreva as mudanças realizadas e envie o PR.
5. Outros membros podem revisar, comentar e sugerir mudanças.
6. Após aprovação, o PR é "mergeado" (integrado) à branch de destino.

### Boas práticas

- Escreva descrições claras e objetivas.
- Faça PRs pequenos e focados em um objetivo.
- Sempre revise o código antes de solicitar revisão.
- Responda comentários e esteja aberto a sugestões.

---
