import {
    createStyles,
    Paper,
    Title,
    Text,
    TextInput,
    Button,
    Container,
    Group,
    Anchor,
    Center,
    Box,
    rem,
} from '@mantine/core';
import { IconArrowLeft } from '@tabler/icons-react';
import { Link } from 'react-router-dom';

const useStyles = createStyles((theme) => ({
    title: {
        fontSize: rem(26),
        fontWeight: 900,
        fontFamily: `Greycliff CF, ${theme.fontFamily}`,
    },

    controls: {
        [theme.fn.smallerThan('xs')]: {
            flexDirection: 'column-reverse',
        },
    },

    control: {
        [theme.fn.smallerThan('xs')]: {
            width: '100%',
            textAlign: 'center',
        },
    },
}));

export function ForgotPassword() {
    const { classes } = useStyles();

    return (
        <Container size={460} my={30}>
            <Title className={classes.title} align="center">
                Forgot your password?
            </Title>
            <Text c="dimmed" fz="lg" ta="center">
                Enter your email to get a reset link
            </Text>

            <Paper withBorder shadow="md" p={30} radius="md" mt="xl">
                <TextInput label="Your email" placeholder="me@mantine.dev" required />
                <Group position="apart" mt="lg" className={classes.controls}>
                    <Link to="/login" color="dimmed" size="sm" className={classes.control}>
                        <Center inline>
                            <IconArrowLeft size={rem(12)} stroke={1.5} />
                            <Box ml={5}>Back to the login page</Box>
                        </Center>
                    </Link>
                    <Button className={classes.control}
                        style={{
                            backgroundColor: "#Fba10d",
                        }}
                    >Reset Password</Button>
                </Group>
            </Paper>
        </Container>
    );
}