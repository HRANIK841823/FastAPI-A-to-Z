import { Link } from "react-router-dom";

import { useAuth } from "../context/AuthContext";


function Navbar() {

  const {
    user,
    isAuthenticated,
    logout
  } = useAuth();


  return (
    <nav>

      <Link to="/">
        Home
      </Link>


      {isAuthenticated ? (

        <>
          <Link to="/profile">
            Profile
          </Link>

          <span>
            Hello {user?.username}
          </span>

          <button onClick={logout}>
            Logout
          </button>
        </>

      ) : (

        <>
          <Link to="/login">
            Login
          </Link>

          <Link to="/register">
            Register
          </Link>
        </>

      )}

    </nav>
  );
}


export default Navbar;