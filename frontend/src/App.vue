<template>
  <div id="app">
    <div>
      <Scatterplot 
        id="comp1" 
        :data="points"
        :selection="[]" 
        :encoding="{ x: 'West-East', y: 'North-South' }"
        @brush="onBrush" 
      />
    </div>
    <!--
    <div>
      <Scatterplot 
        id="comp2" 
        :data="points" 
        :selection="selection" 
        :encoding="{ x: 'attrA', y: 'attrC' }"
      />
    </div>
     -->
    </div>
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
    }
  },
  methods: {
    onBrush(selectedPts) {
      // 有新数据时，更新另一张图
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
