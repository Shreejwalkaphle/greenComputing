import { useState } from "react";

export default function App() {
  const [form, setForm] = useState({
    hardware: "A100",
    devices: 1,
    hours: 1,
    country: "USA",
  });

  const [result, setResult] = useState(null);

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

      {result && (
        <div style={{ marginTop: 20 }}>
          <h3>Result</h3>
          <p>Energy: {result.energy_kwh} kWh</p>
          <p>Carbon: {result.carbon_kg} kg CO₂</p>
          <p>Green Score: {result.green_score}</p>
        </div>
      )}
    </div>
  );
}
