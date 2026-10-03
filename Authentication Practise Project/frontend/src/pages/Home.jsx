import { useAuth } from "../context/AuthContext";

function Home() {

  const {
    user,
    isAuthenticated
  } = useAuth();


  return (
    <div>

      {isAuthenticated ? (

        <h1>
          Welcome {user?.username}
        </h1>

      ) : (

        <h1>
          Welcome Guest
        </h1>

      )}

    </div>
  );
}


export default Home;