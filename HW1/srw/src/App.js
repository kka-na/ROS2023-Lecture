import React from "react";
import { ThemeProvider } from "@material-ui/core";
import mainTheme from "./mainTheme";
import Visualization from "./pages/visualize/Visualization";

function App() {
  return (
    <ThemeProvider theme={mainTheme}>
      <Visualization />
    </ThemeProvider>
  );
}

export default App;