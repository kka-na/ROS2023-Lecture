import React, { useState } from "react";
import { Box} from "@material-ui/core";

import RosSubViz from "../../components/RosSub/RosSubViz";
import SetViz from "./SetViz";
import Footer from "../../components/Footer/Footer";

const Visualization = () => {
  const [getSub, setSub] = useState(false);

  const addSub = (bool) => {
    setSub(bool);
  };

  return (
    <Box align="center" m={3} mt={1}>
      <RosSubViz addSub={addSub} />
      <Box mt={1}></Box>
      <SetViz sub={getSub} />
      <Footer />
    </Box>
  );
};

export default Visualization;
