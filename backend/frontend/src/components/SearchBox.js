import React, { useState } from "react";
import { Button, Form } from "react-bootstrap";
import { useNavigate } from "react-router-dom";

function SearchBox() {
  const [keyword, setKeyword] = useState("");

  let history = useNavigate();
  const submitHandler = (e) => {
    e.preventDefault();
    if (keyword.trim()) {
        history(`/?keyword=${keyword}&page=1`);
    }else{
        history("/")
    }
  };
  return (
    <Form onSubmit={submitHandler} inline="true">
      <Form.Control
        type="text"
        name="q"
        onChange={(e) => setKeyword(e.target.value)}
        className="mr-sm-2 ml-sm-5"
      ></Form.Control>
      <Button
      type="submit"
      variant="outline-success"
      className="p-2">
        Submit
      </Button>
    </Form>
  );
}

export default SearchBox;
