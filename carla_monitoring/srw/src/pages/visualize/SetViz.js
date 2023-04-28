import React, { useState } from "react";
import ROSLIB from "roslib";
import VizStyles from "./VizStyles";
import { CardMedia,Grid, Box} from "@material-ui/core";

const ros = new ROSLIB.Ros({ url: "ws://localhost:9090" });

const detectionTopic = new ROSLIB.Topic({
  ros: ros,
  name: "/darknet_ros/detection_image/compressed",
  messageType: "sensor_msgs/CompressedImage",
});

const warningTopic = new ROSLIB.Topic({
  ros: ros,
  name: "/test/warning",
  messageType: "std_msgs/Int8",
});

const doCaptureTopic = new ROSLIB.Topic({
  ros: ros,
  name: "/test/web/do_capture",
  messageType: "std_msgs/Int8",
});

const SetViz = (props) => {
  const classes = VizStyles();
  const [receiveDetection, setReceiveDetection] = useState([]);
  const [receiveWarning, setReceiveWarning] = useState(0);
  const [isSub, setIsSub] = useState(false);

  if (!isSub && props.sub) {
    setIsSub(true);
    detectionTopic.subscribe(function (message) {
      let image = new Image();
      image.src = "data:image/jpg;base64," + message.data;
      setReceiveDetection(image);
    });
    warningTopic.subscribe(function (message) {
      setReceiveWarning(message.data)
    });
  }

  const doCaptureCam = () => {
    if (isSub) {
      doCaptureTopic.publish({ data: 1 });
    }
  }

  const doCaptureDetection = () => {
    if (isSub) {
      doCaptureTopic.publish({ data: 2 });
    }
  }

  if (isSub && !props.sub) {
    setIsSub(false);
    detectionTopic.unsubscribe();
    warningTopic.unsubscribe();
  }

  return (
    <Grid container spacing={2}>
      <Grid item lg={6}>
        <Box className={classes.warning}>
          {receiveWarning == 1 && <img src="person.png" alt="image" />}
          {receiveWarning == 2 && <img src="car.png" alt="image" />}
        </Box>
      </Grid>
      <Grid item lg={6}>
      <CardMedia
        onClick={doCaptureDetection}
        component="img"
        className={classes.media}
        image={receiveDetection.src}
      />
      </Grid>
    </Grid>     
  );
};

export default SetViz;