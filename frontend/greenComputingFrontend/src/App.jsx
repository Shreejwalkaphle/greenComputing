import { useState } from "react";

export default function App() {
  const [form, setForm] = useState({
    hardware: "A100",
    devices: 1,
    hours: 1,
    country: "USA",
  });

  const [result, setResult] = useState(null);
  const [history, setHistory] = useState([]);

  const fetchHistory = async () => {
    const response = await fetch("http://127.0.0.1:8000/history");
    const data = await response.json();
    setHistory(data);
  };

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const submitForm = async () => {
    const response = await fetch("http://127.0.0.1:8000/evaluate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        ...form,
        devices: parseInt(form.devices),
        hours: parseFloat(form.hours),
      }),
    });

    const data = await response.json();
    setResult(data);
  };

  return (
    <div style={{ padding: 40 }}>
      <h2>Green Computing Evaluation</h2>

      <div>
        <label>Hardware: </label>
        <select name="hardware" onChange={handleChange}>
          <option>A100</option>
          <option>V100</option>
          <option>RTX3090</option>
          <option>CPU</option>
        </select>
      </div>

      <div>
        <label>Devices: </label>
        <input name="devices" type="number" onChange={handleChange} />
      </div>

      <div>
        <label>Training Hours: </label>
        <input name="hours" type="number" onChange={handleChange} />
      </div>

      <div>
        <label>Country: </label>
        <select name="country" onChange={handleChange}>
          <option>USA</option>
          <option>Germany</option>
          <option>India</option>
          <option>Norway</option>
        </select>
      </div>

      <button onClick={submitForm}>Evaluate</button>
      <button onClick={fetchHistory} style={{ marginLeft: 10 }}>
        View History
      </button>

      {result && (
        <div style={{ marginTop: 20 }}>
          <h3>Result</h3>
          <p>Energy: {result.energy_kwh} kWh</p>
          <p>Carbon: {result.carbon_kg} kg CO₂</p>
          <p>Green Score: {result.green_score}</p>

          {result.suggestions && (
            <div style={{ marginTop: 15 }}>
              <h4>Suggestions to Improve</h4>
              <ul>
                {result.suggestions.map((s, i) => (
                  <li key={i}>{s}</li>
                ))}
              </ul>
            </div>
          )}
        </div>
      )}
      {history.length > 0 && (
        <div style={{ marginTop: 30 }}>
          <h3>Past Evaluations</h3>
          <ul>
            {history.map((h, i) => (
              <li key={i}>
                {h.hardware} | {h.devices} devices | {h.hours} hrs | {h.country}{" "}
                → Score: {h.green_score}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}
