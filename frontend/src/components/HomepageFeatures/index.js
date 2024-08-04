import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: 'Easy to Use',
    Svg: require('@site/static/img/undraw_mobile_photos_psm5.svg').default,
    description: (
      <>
        SwasthAI simplifies health management with an intuitive interface, powered by advanced AI for quick disease detection and health insights.
      </>
    ),
  },
  {
    title: 'Focus on What Matters',
    Svg: require('@site/static/img/undraw_active_support_re_b7sj.svg').default,
    description: (
      <>
        Let our AI handle complex medical analysis. Upload your X-rays, MRIs, or blood reports, and our computer vision algorithms do the rest.
      </>
    ),
  },
  {
    title: 'Powered by Smart Technology',
    Svg: require('@site/static/img/undraw_applications_mqwk.svg').default,
    description: (
      <>
        Leverage cutting-edge AI and computer vision in our Android app. SwasthAI brings advanced medical analysis to your fingertips.
      </>
    ),
  },
];

function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
