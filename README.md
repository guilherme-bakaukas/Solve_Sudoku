# Solve Sudoku

O objetivo do projeto é praticar os conceitos de web. O sistema é dividido em frontend e backend, programados em javascript com uso de React e python respectivamente.
O usuário deve colocar o tabuleiro inicial do sudoku, através dos campos de texto e clickar em submmit para submeter os dados iniciais. Assim, o backend irá receber e processar essas informações. A partir desse momento, quando clickar no botão next, o frontend irá requisitar a informação da próxima jogada do sudoku, alterando seu valor no tabuleiro automaticamente. Vale a pena ressaltar que o programa ainda não está inteiramente finalizado e não engloba todas as situações de jogo. Para niveis mais elevados de dificuldade, o programa pode não encontrar uma jogada e irá apresentar um alert para indicar ao usuário. Fique tranquilo! O projeto ainda será incrementado e essas possibilidades de jogo serão analisadas e vinculadas ao algoritmo do jogo...

## Execução do programa
- Frontend
Essa aplicação é gerenciada pelo Node, portanto basta entrar na pasta frontend e executar o comando npm start para rodar a aplicação.

- Backend
Com o python instalado, basta executar o comando python index.py para executar o backend da nossa aplicação

Definimos a porta como localhost:3000 para a comunicação e utilizamos as ferramentas Axios(javascript) e Flask(python) para realizar as requisições necessárias.
Abaixo, há uma introdução as possibiliades de uso da aplicação em react

# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
