/* eslint-disable react/prop-types */
/* eslint-disable react/button-has-type */
import React, { useState, useEffect } from 'react';
import Box from '@material-ui/core/Box';
import Tab from '@material-ui/core/Tab';
import TabContext from '@material-ui/lab/TabContext';
import TabList from '@material-ui/lab/TabList';
import TabPanel from '@material-ui/lab/TabPanel';
import { useSelector, useDispatch } from 'react-redux';
import { makeStyles } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import Divider from '@material-ui/core/Divider';
import { Paper } from '@material-ui/core';
import CartShipForm from '../components/cart/CartShipForm';
import CartReview from '../components/cart/CartReview';
import history from '../history';
import PurchaseCard from '../components/cart/PurchaseCard';
import { fetchCartStatus } from '../actions/index';

const useStyles = makeStyles(() => ({
  root: {
    flexGrow: 1,
    minHeight: '100vh',
  },
}));

export default function Cart({ match }) {
  const cart = useSelector((state) => state.theCart);
  const { cartItems } = cart;

  const artworkId = match.params.workId;
  const dispatch = useDispatch();
  useEffect(() => {
    if (artworkId) {
      dispatch(fetchCartStatus(artworkId));
    }
  }, [dispatch, artworkId]);

  let value;
  console.log(cartItems);

  switch (cartItems) {
    case undefined:
      value = '1';
      break;
    case 'shipping':
      value = '2';
      break;
    default:
      value = '1';
    // code block
  }
  const classes = useStyles();
  return (
    <Grid
      className={classes.root}
      sx={{ marginTop: 5, marginBottom: 10 }}
      container
      direction="row-reverse"
      justifyContent="center"
      spacing={8}
    >
      <Grid item xs={12} md={8}>
        <Box>
          <TabContext value={value}>
            <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
              <TabList
                indicatorColor="secondary"
                aria-label="lab API tabs example"
              >
                <Tab disabled label="آدرس" value="1" />
                <Tab disabled label="تایید" value="2" />
                <Tab disabled label="رسید" value="3" />
              </TabList>
            </Box>
            <TabPanel value="1">
              <CartShipForm match={match} />
            </TabPanel>
            <TabPanel value="2">
              <CartReview />
            </TabPanel>
            <TabPanel value="3">
              <div> hi </div>
            </TabPanel>
          </TabContext>
        </Box>
      </Grid>

      <Grid
        container
        direction="column"
        spacing={8}
        item
        xs={12}
        md={4}
        sx={{ padding: 0 }}
      >
        <Grid item>
          <PurchaseCard workId={match.params.workId} />
        </Grid>
      </Grid>
    </Grid>
  );
}
