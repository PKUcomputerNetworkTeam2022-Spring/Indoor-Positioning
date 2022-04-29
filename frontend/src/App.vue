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
            <b-nav-item href="http://localhost:8000/admin">Admin</b-nav-item>
            
            <!-- Positioning Button -->
            <b-nav-item href="#" v-b-modal.modal-1>Positioning
              <b-modal v-modal="show_modal" id="modal-1" title="Get Position">
                <template #modal-header="{ close }">
                  <h5>Do Positioning</h5>
                </template>
                <b-form inline>
                  <b-row>
                    <b-col cols="8">
                      <b-form-input
                        id="inline-form-input-name"
                        class="mb-2 mr-sm-2 mb-sm-0"
                        v-model="form.mac"
                        placeholder="MAC of the target device."
                      ></b-form-input>
                    </b-col>
                    <b-col>
                      <b-button variant="success" @click="onPosition">Get Position!</b-button>
                    </b-col>
                  </b-row>
                </b-form>

              </b-modal>
            </b-nav-item>
          
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
              <div class='dashboard'>
                <vega-lite :data="trace_points" :mark="{'type': 'point'}" :encoding="encoding" :width="450" :height="470"/>
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
                    <v-circle :config="f4041c_center"></v-circle>
                    <v-circle :config="f40443_center"></v-circle>
                    <v-circle :config="f40444_center"></v-circle>
                    <v-star :config="real_pos"></v-star>
                    <v-regular-polygon :config="pos"></v-regular-polygon>
                    <v-text :config="real_pos_coordinate"></v-text>
                    <v-text :config="pos_coordinate"></v-text>
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
      form: {
        "mac": "",
      },
      selection: [],
      // For Trace Display.
      trace_points: [
        {"West-East": 0.0, "North-South": 0.0, "Type": "sniffing-device"},    // f4041c
        {"West-East": 0.0, "North-South": 10.2, "Type": "sniffing-device"},   // f40443
        {"West-East": 6.47, "North-South": 10.2, "Type": "sniffing-device"},  // f40444
      ],
      encoding: {
        x: {field: 'West-East', type: 'quantitative', scale: { domain: [0, 7] } },
        y: {field: 'North-South', type: 'quantitative', scale: { domain: [0, 11] } },
        color: {
          field: "Type",
          type: "ordinal",
          "scale": {
            "range": [
              "#FA3B12",
              "#123BFA",
            ]
          }
        },
        shape: {field: "Type", type: "ordinal"},
      },
      // For Positioning Detail. 
      configKonva: {
        width: 500,
        height: 520,
        opacity: 0.8
      },
      f4041c: {
        x: 30*0+100,
        y: 450-30*0,
        radius: 1,
        fill: "green",
        stroke: "black",
        strokeWidth: 2
      },
      f4041c_center: {
        x: 30*0+100,
        y: 450-30*0,
        radius: 2,
        fill: "black",
        stroke: "black",
        strokeWidth: 2
      },
      f40443: {
        x: 30*0+100,
        y: 450-30*10.2,
        radius: 1,
        fill: "yellow",
        stroke: "black",
        strokeWidth: 2
      },
      f40443_center: {
        x: 30*0+100,
        y: 450-30*10.2,
        radius: 2,
        fill: "black",
        stroke: "black",
        strokeWidth: 2
      },
      f40444: {
        x: 30*6.4+100,
        y: 450-30*10.2,
        radius: 1,
        fill: "orange",
        stroke: "black",
        strokeWidth: 2
      },
      f40444_center: {
        x: 30*6.4+100,
        y: 450-30*10.2,
        radius: 2,
        fill: "black",
        stroke: "black",
        strokeWidth: 2
      },
      real_pos: {
        x: -100,
        y: -100,
        numPoints: 6,
        innerRadius: 3,
        outerRadius: 5,
        fill: 'red',
        stroke: 'black',
        strokeWidth: 1,
      },
      pos: {
        x: -100,
        y: -100,
        sides: 6,
        radius: 5,
        fill: 'blue',
        stroke: 'black',
        strokeWidth: 1,
      },
      real_pos_coordinate: {
        x: -100,
        y: -100,
        text: "Real Pos: (1.25, 1.25)",
        fontsize: 18,
        fontFamily: "Calibri",
        fill: "black",
      },
      pos_coordinate: {
        x: -100,
        y: -100,
        text: "Estimated Pos: (1.00, 1.50)",
        fontsize: 18,
        fontFamily: "Calibri",
        fill: "black",
      }
    }
  },
  methods: {
    onPosition() {
      // Shows one positioning result on the UI.
      const path = "http://localhost:8000/api";
      let that = this;
      axios.post(path, {
        "mac": this.form["mac"]
        },
        {
          headers: {"Access-Control-Allow-Origin": "*"}
        }).then(function (response) {
        console.log("i accept");
        console.log(response.data);
        var pos = response.data["position"][0];
        var dist = response.data["distances"][0];
        that.pos["x"] = 30 * pos[0] + 100;
        that.pos["y"] = 450 - 30 * pos[1];
        that.f4041c["radius"] = 30 * dist[0][1];
        that.f40443["radius"] = 30 * dist[1][1];
        that.f40444["radius"] = 30 * dist[2][1];
        that.trace_points.push({"West-East": pos[0], "North-South": pos[1], "Type": "point"});
      });
    }
  },
}
</script>

<style>
#app {

}
</style>