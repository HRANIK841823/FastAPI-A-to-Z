import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";


import Navbar from "./components/Navbar";

import ProtectedRoute from "./components/ProtectedRoute";

import Home from "./pages/Home";

import Login from "./pages/Login";

import Register from "./pages/Register";

import Profile from "./pages/Profile";


function App() {

  return (

    <BrowserRouter>

      <Navbar />

      <Routes>

        {/* Public page */}
        <Route
          path="/"
          element={<Home />}
        />


        {/* Public page */}
        <Route
          path="/login"
          element={<Login />}
        />


        {/* Public page */}
        <Route
          path="/register"
          element={<Register />}
        />


        {/* Protected page */}
        <Route
          path="/profile"
          element={
            <ProtectedRoute>
              <Profile />
            </ProtectedRoute>
          }
        />

      </Routes>

    </BrowserRouter>
  );
}


export default App;