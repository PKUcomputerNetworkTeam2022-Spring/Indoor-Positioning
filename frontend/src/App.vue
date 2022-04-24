<style scoped>
 .navbar.navbar-dark.bg-dark{
    background-color: #AABB55!important;
 }
</style>

<template>
  <div id="app">
    <!-- NavBar -->
    <div>
      <b-navbar toggleable="lg" type="dark" variant="dark">
        <div class="container">
          <b-navbar-brand href="#">Indoor Positioning</b-navbar-brand>
        </div>
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
            <b-nav-item href="#">Admin</b-nav-item>
            <b-nav-item href="#">Positioning</b-nav-item>
          </b-navbar-nav>

        </b-collapse>
      </b-navbar>
    </div>

    <b-container class="bv-example-row">
      <b-row>
        <b-col>
          <!-- Scatter Plot for Track Display -->
          <div class="shadow p-3 mb-5 bg-white rounded">
            <b-card
              title="Track Display"
              style="max-width: 80rem;"
              class="mb-2"
            >
              <div>
                <Scatterplot 
                  id="comp1" 
                  :data='[]'
                  :selection="[]" 
                  :encoding="{ x: 'West-East', y: 'North-South' }"
                  @brush="onBrush" 
                />
              </div>
            </b-card>
          </div>
        </b-col>
        <b-col>
          <!-- Draw Circle to Show Positioning -->
          <div class="shadow p-3 mb-5 bg-white rounded">
            <b-card
              title="Positioning Detail"
              style="max-width: 80rem;"
              class="mb-2"
            >
              <div>
                <v-stage :config="configKonva">
                  <v-layer>
                    <v-circle :config="f4041c"></v-circle>
                    <v-circle :config="f40443"></v-circle>
                    <v-circle :config="f40444"></v-circle>
                    <v-star :config="real_pos"></v-star>
                    <v-regular-polygon :config="pos"></v-regular-polygon>
                  </v-layer>
                </v-stage>
              </div>
            </b-card>
          </div>
        </b-col>
      </b-row>
    </b-container>
    
  </div>
</template>

<script>
import Scatterplot from './components/Scatterplot'
import _ from 'lodash'

export default {
  props: {

    points: {
      type: Array,
      required: true,
    },

  },
  data () {
    return {
      selection: [],
      configKonva: {
        width: 500,
        height: 520,
        opacity: 0.5
      },
      f4041c: {
        x: 100,
        y: 100,
        radius: 70,
        fill: "green",
        stroke: "black",
        strokeWidth: 2
      },
      f40443: {
        x: 150,
        y: 150,
        radius: 70,
        fill: "yellow",
        stroke: "black",
        strokeWidth: 2
      },
      f40444: {
        x: 200,
        y: 200,
        radius: 70,
        fill: "orange",
        stroke: "black",
        strokeWidth: 2
      },
      real_pos: {
        x: 125,
        y: 125,
        numPoints: 6,
        innerRadius: 3,
        outerRadius: 5,
        fill: 'red',
        stroke: 'black',
        strokeWidth: 1,
      },
      pos: {
        x: 100,
        y: 150,
        sides: 6,
        radius: 5,
        fill: 'blue',
        stroke: 'black',
        strokeWidth: 1,
      }
    }
  },
  methods: {
    onBrush(selectedPts) {
      const newPts = _.differenceBy(selectedPts, this.selection, 'id')
      if (newPts.length > 0) {
        this.selection = selectedPts
      }
    }
  },
  components: {
    Scatterplot
  }
}
</script>

<style>
#app {

}
</style>