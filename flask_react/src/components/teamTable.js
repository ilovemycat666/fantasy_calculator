import React, {useState} from "react";
import './teamTable.css';

const TeamTable = (teamsData) => {
    const [savedTeam, setSavedTeam] = useState([])

    const handleSubmit = event => {
        event.preventDefault();
        savedTeam.forEach((player) => {
            console.log(player[0])
        })
    }

    const rows = [];
    if (teamsData !== undefined) {
        const teamData = teamsData.teamsData;
        if (teamData.length <= 9) {
            const bad_picks = []
            teamData.forEach((bad_pick) => {
                bad_picks.push(
                    <li>{bad_pick}</li>
                )
            });
            return (
                <div>
                    <h4>bad picks, try again:</h4>
                    <ul>
                        {bad_picks && bad_picks}
                    </ul>
                </div>
            )
        }
        else {
            teamData.forEach((team) => {
                team[2].forEach((player) => {
                    rows.push(
                        <tr>
                            <td>{player[0]}</td>
                            <td>{player[1]}</td>
                            <td>{player[2]}</td>
                            <td>{player[3]}</td>
                            <td>{player[4]}</td>
                            <td>{player[5]}</td>
                            <td>{player[6]}</td>
                            <td>{player[7]}</td>
                        </tr>
                    )
                });
                rows.push(<tr><td>Points: {team[0]}</td></tr>);
                rows.push(<tr><td>Salary: {team[1]}</td></tr>);
                rows.push(
                    <tr>
                        <td>
                            <div>
                                <form onSubmit={handleSubmit}>
                                    <button type="submit" onClick={event => setSavedTeam(team[2])}>Save this team</button>
                                </form>
                            </div>
                        </td>
                    </tr>
                );
            });
        }
    }

    
    return (
        <div>
            <table>
                <thead>
                    <tr>
                        <th>id</th>
                        <th>position</th>
                        <th>name</th>
                        <th>salary</th>
                        <th>fppg</th>
                        <th>value</th>
                        <th>game</th>
                        <th>team</th>
                    </tr>
                </thead>
                <tbody>
                    {rows && rows}
                </tbody>
            </table>
        </div>
    );
}

export default TeamTable;



                                // <form onclick={() => { saveTeam(team[2]) }}>
                                //     <button>Save This Team</button>
                                // </form>

                                {/* <form onSubmit={handleSubmit}>
                                    <input
                                        type="hidden"
                                        id="saveTeam"
                                        name="saveTeam"
                                        value={team[2]}
                                        onClick={event => setSavedTeam(event.target.value)}
                                    />
                                    <button type="submit">Save this team</button>
                                </form> */}