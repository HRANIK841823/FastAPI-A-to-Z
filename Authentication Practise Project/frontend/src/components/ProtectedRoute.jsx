import { Navigate } from "react-router-dom";

import { useAuth } from "../context/AuthContext";


function ProtectedRoute({ children }) {

  const {
    isAuthenticated,
    loading
  } = useAuth();


  // Wait until authentication check finishes
  if (loading) {

    return <h2>Loading...</h2>;
  }


  // Not logged in
  if (!isAuthenticated) {

    return (
      <Navigate
        to="/login"
        replace
      />
    );
  }


  // Logged in
  return children;
}


export default ProtectedRoute;