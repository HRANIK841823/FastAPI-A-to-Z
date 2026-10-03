import { createContext, useContext, useEffect, useState } from "react";

const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
  const [token, setToken] = useState(localStorage.getItem("token"));
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  // ব্যাকএন্ড থেকে বর্তমান ইউজারের তথ্য আনা
  const getCurrentUser = async (accessToken) => {
    try {
      const response = await fetch("http://127.0.0.1:8000/me", {
        headers: { Authorization: `Bearer ${accessToken}` },
      });

      if (!response.ok) {
        localStorage.removeItem("token");
        setToken(null);
        setUser(null);
        return;
      }

      const data = await response.json();
      setUser(data);
    } catch (error) {
      console.error("Failed to fetch user:", error);
      setUser(null);
    } finally {
      setLoading(false);
    }
  };

  // অ্যাপ লোড হওয়ার সময় আগের লগইন স্টেট চেক করা
  useEffect(() => {
    const savedToken = localStorage.getItem("token");
    if (savedToken) {
      setToken(savedToken);
      getCurrentUser(savedToken);
    } else {
      setLoading(false);
    }
  }, []);

  // লগইন হ্যান্ডলার
  const login = async (email, password) => {
    const formData = new FormData();
    formData.append("email", email);
    formData.append("password", password);

    const response = await fetch("http://127.0.0.1:8000/login", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    if (!response.ok) throw new Error(data.detail || "Login failed");

    localStorage.setItem("token", data.access_token);
    setToken(data.access_token);
    await getCurrentUser(data.access_token);
  };

  // লগআউট হ্যান্ডলার
  const logout = () => {
    localStorage.removeItem("token");
    setToken(null);
    setUser(null);
  };

  const value = {
    token,
    user,
    loading,
    isAuthenticated: !!token,
    login,
    logout,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};

export const useAuth = () => useContext(AuthContext);