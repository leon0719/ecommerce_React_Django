import { Container } from "react-bootstrap";
import Header from "./components/Header";
import Footer from "./components/Footer";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import HomeScreen from "./screens/HomeScreen";
import ProductScreen from "./screens/ProductScreen";

function App() {
  return (
    <Router>
      <Header></Header>
      <main className="py-3">
        <Container>
        <Routes>
        <Route path='/' element={<HomeScreen></HomeScreen>} />
        <Route path='/product/:id' element={<ProductScreen></ProductScreen>} />
        </Routes>
        </Container>
      </main>
      <Footer></Footer>
    </Router>
  );
}

export default App;
