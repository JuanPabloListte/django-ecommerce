import { BrowserRouter, Routes, Route } from "react-router-dom"
import Layout from "./components/layout"
import HomePage from "./pages/HomePage"

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route path="/" element={<HomePage />}></Route>
        </Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App
