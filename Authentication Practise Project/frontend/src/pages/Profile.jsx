import { useAuth } from "../context/AuthContext";


function Profile() {

  const {
    user,
    logout
  } = useAuth();


  return (
    <div>

      <h1>My Profile</h1>


      <img
        src={`http://127.0.0.1:8000/uploads/${user.image}`}
        alt="Profile"
        width="150"
        height="150"
      />


      <h2>
        {user.username}
      </h2>


      <p>
        {user.email}
      </p>


      <button onClick={logout}>
        Logout
      </button>

    </div>
  );
}


export default Profile;