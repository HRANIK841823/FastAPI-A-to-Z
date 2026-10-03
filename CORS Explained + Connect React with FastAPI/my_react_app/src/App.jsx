import React, { useState, useEffect } from "react";

const App = () => {
  // API থেকে পাওয়া data রাখার জন্য state
  const [data, setData] = useState(null);

  // Component load হওয়ার পর API call হবে
  useEffect(() => {
    fetch("http://127.0.0.1:8000/")
      .then((response) => response.json())
      .then((json) => setData(json))
      .catch((error) => console.error("Error fetching API:", error));
  }, []);

  return (
    <div>
      <h1>API Data</h1>

      {data ? (
        <p>Message: {data.message}</p>
      ) : (
        <p>Loading....</p>
      )}
    </div>
  );
};

export default App;