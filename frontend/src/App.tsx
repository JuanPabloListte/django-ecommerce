import { BrowserRouter, Routes, Route } from "react-router-dom"
import Layout from "./components/Layout"
import HomePage from "./pages/HomePage"
import LoginPage from "./pages/LoginPage"
import ResgisterPage from "./pages/RegisterPage"


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<HomePage />}></Route>
          <Route path="login" element={<LoginPage />}></Route>
          <Route path="register" element={<ResgisterPage />}></Route>
        </Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App
