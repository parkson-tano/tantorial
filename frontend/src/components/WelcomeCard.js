import { createStyles, Card, Image, Avatar, Text, Group, UnstyledButton } from '@mantine/core';
import { useNavigate } from 'react-router-dom';

const useStyles = createStyles((theme) => ({
    card: {
        backgroundColor: theme.colorScheme === 'dark' ? theme.colors.dark[7] : theme.white,
    },

    title: {
        fontWeight: 700,
        fontFamily: `Greycliff CF, ${theme.fontFamily}`,
        lineHeight: 1.2,
    },

    body: {
        padding: theme.spacing.md,
    },
}));

export default function WelcomeCard({
    image,
    description,
    title,
    url

}) {
    const { classes } = useStyles();
    const navigate = useNavigate();
    return (
        <Card withBorder radius="md" p={0} className={classes.card}
        >   <UnstyledButton onClick={() => navigate(url)}>
                <Group noWrap spacing={0}>
                    <Image src='https://images.unsplash.com/photo-1602080858428-57174f9431cf?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=400&q=80' height={140} width={140} />
                    <div className={classes.body}>
                        <Text transform="uppercase" className={classes.title} mt="xs" mb="md" fz="xl">
                            {title}
                        </Text>
                        <Text weight={500} size="lg">
                            {description}
                        </Text>
                    </div>

                </Group>
            </UnstyledButton>
        </Card>
    );
}