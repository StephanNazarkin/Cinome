import logo from './logo.svg';
import './App.css';

function App() {
  const sendRequest = async () => {
    const response = await fetch('http://localhost:8000/api/test/');

    if (!response.ok) {
      throw new Error(`Error! status: ${response.status}`);
    }

    const result = await response.json();
    console.log(JSON.stringify(result, null));
  };

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <button onClick={sendRequest}>
          Send a request!
        </button>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
