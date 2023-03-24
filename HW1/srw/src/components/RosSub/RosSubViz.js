import React, { useEffect, useState } from "react";
import {
  ToggleButton,
  Grid,
  ToggleButtonGroup,
} from "@mui/material";
import SharedStyles from "./SharedStyles";
import Weather from "../Weather/Weather";

const RosSubViz = ({ addSub }) => {
  const classes = SharedStyles();
  const [time, setTime] = useState(0);
  const [sub, setSub] = useState(false);

  useEffect(() => {
    let interval = null;
    return () => {
      clearInterval(interval);
    };
  }, [sub]);

  const handleChange = (event, newSub) => {
    let sub_n;
    if (newSub === null) {
      sub_n = sub;
    } else if (newSub) {
      sub_n = newSub;
      setTime(0);
      addSub(true);
    } else if (!newSub) {
      sub_n = newSub;
      addSub(false);
    }
    setSub(sub_n);
  };

  return (
    <Grid container spacing={2}>
      <Grid item xs={3} className={classes.text}>
        <Weather />
      </Grid>
      <Grid item xs={7}></Grid>
      <Grid item xs={2} className={classes.grid}>
        <ToggleButtonGroup
          className={classes.toggle_button_group}
          value={sub}
          exclusive
          onChange={handleChange}
          fullWidth
        >
          <ToggleButton className={classes.toggle_button} value={true}>
            Subscribe
          </ToggleButton>

          <ToggleButton className={classes.toggle_button} value={false}>
            Unsubscribe
          </ToggleButton>
        </ToggleButtonGroup>
      </Grid>
    </Grid>
  );
};

export default RosSubViz;
