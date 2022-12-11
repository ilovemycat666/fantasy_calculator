import { useState } from 'react'
import axios from "axios";
import Header from './components/header';
import TeamTable from './components/teamTable';
import './App.css';
// import PlayerPicker from './components/playerPicks';

function App() {
  const [teamsData, setTeamsData] = useState(null);
  const [playerPicks, setPlayerPicks] = useState("");
  const [file, setFile] = useState();
  const [loading, setLoading] = useState(false);



  const getData = async (e) => {
    e.preventDefault();
    setLoading(true);
    setTeamsData(null);
    
    if (file) {
      const fileReader = new FileReader();
      fileReader.readAsText(file);
      fileReader.onload = async (event) => {
        const text = event.target.result;

        const csvRows = text.slice(text.indexOf("\n") + 1).split("\n");
        const fanduelCsv = []
        csvRows.forEach(element => {
          fanduelCsv.push(csvRows);
        });

        const formData = new FormData();
        formData.append('fanduelCsv', JSON.stringify(fanduelCsv));
        formData.append('playerPicks', playerPicks);

        await axios.post(
          '/createTeams',
          formData,
          {
            headers: {'Content-Type': 'multipart/form-data'}
          }
        ).then((response) => {
          console.log("success");
          const res = response.data
          setTeamsData(res) 
          setLoading(false)
        }).catch((error) => {
          console.log("failure");
          setLoading(false);
          if (error.response) {
            console.log(error.response)
            console.log(error.response.status)
            console.log(error.response.headers)
            }
        })

      };
    }
  }


  return (
    <div className="App">
      <header className="App-header">
        <Header />
        <form>
          <input
            type={"file"}
            id={"csvFileInput"}
            accept='.csv'
            onChange={(e) => setFile(e.target.files[0])} />
          <div>
            <label>Player Lock</label>
            <br></br>
            <input type='text' placeholder='enter desired players' onChange={(e) => setPlayerPicks(e.target.value)}/>
          </div>
          <button onClick={getData} >Click me</button>
        </form>
        {loading && <div>Loading...</div>}
        {teamsData && <TeamTable teamsData={teamsData} />}
      </header>
    </div>
  );
}

export default App;
