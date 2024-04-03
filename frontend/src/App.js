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
import PlaceOrderScreen from "./screens/PlaceOrderScreen";
import OrderScreen from "./screens/OrderScreen";
import UserListScreen from "./screens/UserListScreen";
import UserEditScreen from "./screens/UserEditScreen";
import ProductListScreen from './screens/ProductListScreen'
import ProductEditScreen from './screens/ProductEditScreen'

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
        <Route path='/placeorder' element={<PlaceOrderScreen></PlaceOrderScreen>} />
        <Route path='/order/:id' element={<OrderScreen></OrderScreen>} />
        <Route path='/payment' element={<PaymentScreen></PaymentScreen>} />
        <Route path='/product/:id' element={<ProductScreen></ProductScreen>} />
        <Route path='/cart/:id?' element={<CartScreen></CartScreen>} />
        <Route path='/admin/userlist' element={<UserListScreen></UserListScreen>} />
        <Route path='/admin/user/:id/edit' element={<UserEditScreen></UserEditScreen>} />
        <Route path='/admin/productlist' element={<ProductListScreen></ProductListScreen>} />
        <Route path='/admin/product/:id/edit' element={<ProductEditScreen></ProductEditScreen>} />
        </Routes>
        </Container>
      </main>
      <Footer></Footer>
    </Router>
  );
}

export default App;
