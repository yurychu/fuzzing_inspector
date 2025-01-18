<template>
  <div class="item">
    <i>
      <slot name="icon"></slot>
    </i>

    <div class="details">
      <h3>
        <slot name="heading"></slot>
      </h3>

      <slot></slot>

    </div>

  </div>
</template>


<style scoped>

.item {
  margin-top: 2rem;
  /* display: flex; */
  /* position: relative; */
}

@media (min-width: 1024px) {
  .item {

    padding: 0.4rem 0 1rem calc(var(--section-gap) / 4);
  }

}
</style>