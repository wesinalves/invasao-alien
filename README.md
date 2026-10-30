# Invasão Alien

Projeto da disciplina de programação orientada a objetos. O objetivo é implementar o jogo Invasão Alien usando pygame.

## Como contribuir

- Dê uma **estrela** (*Star*) neste repositório.
- Verifique os scripts existentes no diretório `projetos`.
- Na página do repositório [Invasão Alien](https://github.com/wesinalves/invasao-alien), clique no botão **Fork**. 
<br><img src="https://docs.github.com/assets/images/help/repository/fork-button.png" title="Imagem do botão Fork" width="400"/>
- **Clone** o repositório que você acabou de fazer o *fork* para sua máquina local. Este botão mostrará a URL que você deve usar. 
<br><img src="https://docs.github.com/assets/images/help/repository/code-button.png" title="Botão Code" width="400"/>

Por exemplo, execute este comando no seu terminal:

```bash
git clone https://github.com/<seu-nome-de-usuario-no-github>/invasao-alien.git
```

**Substitua \<seu-nome-de-usuario-no-github\>!**

Saiba mais sobre como fazer *fork* ([forking](https://help.github.com/en/github/getting-started-with-github/fork-a-repo)) e como clonar um repositório ([cloning a repo](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)).
- Antes de fazer qualquer alteração, [mantenha seu *fork* sincronizado](https://www.freecodecamp.org/news/how-to-sync-your-fork-with-the-original-git-repository/) para evitar conflitos de *merge*:

```bash
git remote add upstream https://github.com/wesinalves/invasao-alien.git
git fetch upstream
git pull upstream main
git push
```

Alternativamente, o GitHub agora também oferece sincronização: clique em "Fetch upstream" no topo do seu repositório, logo abaixo do botão "Code".

- Se você encontrar um **conflito de *merge***, precisará resolvê-lo. Existem muitos guias online, ou você pode consultar este do [opensource.com](https://opensource.com/article/20/4/git-merge-conflict).

- Mude para uma nova branch de desenvolvimento (*nomeie sua branch de acordo com o nome da issue*). 

```bash
git checkout -b <nome-da-branch>
```

- Adicione as alterações com `git add` e `git commit` ([escreva uma boa mensagem de commit](https://chris.beams.io/posts/git-commit/), se possível):

```bash
git add -A
git commit -m "<sua-mensagem>"
```

- Envie (push) o código _para o seu repositório_. 

```bash
git push origin <nome-da-branch>
```

- Vá para a página do GitHub do *seu fork* e **crie um pull request**:

![imagem de pull request](https://docs.github.com/assets/cb-34097/mw-1440/images/help/pull_requests/pull-request-compare-pull-request.webp)

Leia mais sobre pull requests nas [páginas de ajuda do GitHub](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).
- Agora, aguarde até *revisão do seu Pull Request*! Se houver conflitos, você receberá uma notificação.

# Referências:

- [Documentação do Pygame](https://pyga.me/docs/)

