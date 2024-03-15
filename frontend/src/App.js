import { Container } from "react-bootstrap";
import Header from "./components/Header";
import Footer from "./components/Footer";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import HomeScreen from "./screens/HomeScreen";
import ProductScreen from "./screens/ProductScreen";
import CartScreen from "./screens/CartScreen";
import LoginScreen from "./screens/LoginScreen";
import RegisterScreen from "./screens/RegisterScreen";
import ProfileScreen from "./screens/ProfileScreen";
import ShippingScreen from "./screens/ShippingScreen";
import PaymentScreen from "./screens/PaymentScreen";

function App() {
  return (
    <Router>
      <Header></Header>
      <main className="py-3">
        <Container>
        <Routes>
        <Route path='/' element={<HomeScreen></HomeScreen>}/>
        <Route path='/login' element={<LoginScreen></LoginScreen>} />
        <Route path='/register' element={<RegisterScreen></RegisterScreen>} />
        <Route path='/profile' element={<ProfileScreen></ProfileScreen>} />
        <Route path='/shipping' element={<ShippingScreen></ShippingScreen>} />
        <Route path='/payment' element={<PaymentScreen></PaymentScreen>} />
        <Route path='/product/:id' element={<ProductScreen></ProductScreen>} />
        <Route path='/cart/:id' element={<CartScreen></CartScreen>} />
        </Routes>
        </Container>
      </main>
      <Footer></Footer>
    </Router>
  );
}

export default App;
